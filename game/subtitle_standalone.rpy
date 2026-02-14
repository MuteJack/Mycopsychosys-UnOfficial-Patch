# Standalone Subtitle Function for Mycopsychosis
# Developed by Mute Jack (UnOfficial)
# Just place this file and a VTT file into the game/ folder.
#   - game/MYCOPSYCHOSIS.vtt (default fallback)
#   - game/tl/{lang}/MYCOPSYCHOSIS.vtt (language-specific)
# And place MYCOPSYCHOSIS.vtt(eng) to game/ folder.
# To Translate the subtitles, place translated MYCOPSYCHOSIS.vtt file to game/tl/{language} folder.

init python:
    import re
    import os
    import time as pytime

    def parse_vtt_time(time_str):
        """Convert VTT timestamp (HH:MM:SS.mmm or MM:SS.mmm) to seconds"""
        parts = time_str.strip().split(':')
        if len(parts) == 3:
            h, m, s = parts
        else:
            h = 0
            m, s = parts
        s = s.replace(',', '.')
        return int(h) * 3600 + int(m) * 60 + float(s)

    def load_vtt_subtitles(full_path):
        """Parse VTT file and return list of (start, end, text) tuples"""
        subtitles = []
        if not os.path.exists(full_path):
            return subtitles
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return subtitles

        lines = content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Skip NOTE comment blocks
            if line.startswith('NOTE'):
                i += 1
                while i < len(lines) and lines[i].strip() and not re.match(r'^\d+$', lines[i].strip()) and '-->' not in lines[i]:
                    i += 1
                continue
            # Parse timestamp line (e.g. "00:01:23.456 --> 00:01:25.789")
            if '-->' in line:
                match = re.match(r'(\d+:\d+:\d+\.\d+|\d+:\d+\.\d+)\s*-->\s*(\d+:\d+:\d+\.\d+|\d+:\d+\.\d+)', line)
                if match:
                    start = parse_vtt_time(match.group(1))
                    end = parse_vtt_time(match.group(2))
                    i += 1
                    # Collect multi-line subtitle text
                    text_lines = []
                    while i < len(lines) and lines[i].strip() and not re.match(r'^\d+$', lines[i].strip()) and '-->' not in lines[i] and not lines[i].strip().startswith('NOTE'):
                        text_lines.append(lines[i].strip())
                        i += 1
                    if text_lines:
                        subtitles.append((start, end, '\n'.join(text_lines)))
                    continue
            i += 1
        return subtitles

    # --- Subtitle state ---
    subtitle_cache = {}       # Cache: {language: [(start, end, text), ...]}
    subtitle_enabled = True   # Subtitle visibility toggle
    _sub_auto_start = 0.0     # Timestamp when movie playback was detected
    _sub_movie_was_playing = False  # Tracks whether a movie is currently playing

    def toggle_subtitle():
        """Toggle subtitle on/off"""
        global subtitle_enabled
        subtitle_enabled = not subtitle_enabled
        renpy.restart_interaction()

    def _is_movie_playing():
        """Auto-detect movie playback via renpy.showing() — no intro.rpy modification needed"""
        return renpy.showing("video") or renpy.showing("videoesp")

    def get_subtitles_for_lang():
        """Load subtitles for current language, with fallback to default VTT"""
        lang = _preferences.language
        if lang in subtitle_cache:
            return subtitle_cache[lang]

        game_dir = renpy.config.gamedir

        # Try language-specific VTT first (game/tl/{lang}/MYCOPSYCHOSIS.vtt)
        if lang is not None:
            lang_path = os.path.join(game_dir, "tl", lang, "MYCOPSYCHOSIS.vtt")
            subs = load_vtt_subtitles(lang_path)
            if subs:
                subtitle_cache[lang] = subs
                return subs

        # Fallback to default VTT (game/MYCOPSYCHOSIS.vtt)
        default_path = os.path.join(game_dir, "MYCOPSYCHOSIS.vtt")
        subs = load_vtt_subtitles(default_path)
        subtitle_cache[lang] = subs
        return subs

    def get_current_subtitle_auto():
        """Return subtitle text matching current video time.
        Automatically starts timing when movie is detected on screen."""
        global _sub_auto_start, _sub_movie_was_playing

        # No movie on screen — reset state
        if not _is_movie_playing():
            _sub_movie_was_playing = False
            return ""

        # Movie just started — record start time
        if not _sub_movie_was_playing:
            _sub_auto_start = pytime.time()
            _sub_movie_was_playing = True

        # Find subtitle matching elapsed time
        current_time = pytime.time() - _sub_auto_start
        for start, end, text in get_subtitles_for_lang():
            if start <= current_time <= end:
                return text
        return ""

    # Register as overlay screen — always active, shows content only during movie playback
    config.overlay_screens.append("video_subtitle")

screen video_subtitle():
    # Refresh every 0.1s for subtitle timing
    timer 0.1 repeat True action Function(renpy.restart_interaction)

    $ current_sub = get_current_subtitle_auto()

    # Only show UI when a movie is playing
    if _is_movie_playing():
        if _preferences.language == "korean":
            $ _sub_label = "자막 끄기" if subtitle_enabled else "자막 켜기"
        else: # Default Language(English)
            $ _sub_label = "Subtitles OFF" if subtitle_enabled else "Subtitles ON"
        textbutton _sub_label:
            xalign 0.9
            yalign 0.18
            text_size 20
            text_color "#ffffff"
            background "#000000aa"
            padding (10, 5)
            action Function(toggle_subtitle)

    # Subtitle text display
    if subtitle_enabled and current_sub:
        frame:
            xalign 0.5
            yalign 0.9
            background "#000000aa"
            padding (20, 10)
            text current_sub:
                substitute False
                color "#ffffff"
                size 28
                text_align 0.5
                xalign 0.5
