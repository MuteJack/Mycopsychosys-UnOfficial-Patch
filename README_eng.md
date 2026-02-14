# Mycopsychosys Remastered - Unofficial Feature/Korean Translation Patch

> NOTE: If you want to read this in Korean, check [README_kor.md](README_kor.md)

Unofficial feature patch for Mycopsychosys Remastered.
Including useful features (ex: subtitle for intro video) and Korean translation.
Note that this patch may not work if the game is updated.

As of the 2026.02.14 update, Korean is now officially supported in the game, so the Korean translation has been removed from this patch.
Special thanks to the game development team DeltaCatStudio and developer i3q2 for their interest in supporting the translation.

---

## 0. Information

### 0.1. Version Info

- Game: Mycopsychosys Remastered
- Game Version: Mycopsychosys v2.0 (2026.02.14 Update) or Later
- Patch Version: 1.0.7 (2026.02.15)

### 0.2. Environment Support

- O/S: Windows, macOS, Linux (Ren'Py supported platforms)
- Game Platform: Steam, Itch.io

---

## 1. Installation

1. Purchase and install Mycopsychosys Remastered from Steam.
2. Copy the files inside the `game/` folder to the `game/` folder of your game installation.
   - Files to copy: `subtitle_standalone.rpy`, `MYCOPSYCHOSIS.vtt`, `tl/korean/MYCOPSYCHOSIS.vtt`
   - Default path: `C:\Program Files (x86)\Steam\steamapps\common\Mycopsychosys Remastered\game\`
   - Other path: `{Drive Letter}:\SteamLibrary\steamapps\common\Mycopsychosys Remastered\game\`
3. Launch the game — subtitles will automatically appear during the intro video.

---

## 2. Additional Features / Changes

### 2.1 Intro Video Subtitle System (Subtitle Files and Feature)

Displays subtitles on the intro video in-game.

- Works with `subtitle_standalone.rpy` + VTT files only — no modification to original game files required.
- Default subtitles (English, `game/MYCOPSYCHOSIS.vtt`)
- Translated subtitles (`game/tl/{language}/MYCOPSYCHOSIS.vtt`)
- Since the subtitle files are only in English and Korean, all other languages will be displayed as default language (English).
- If you want to add translated subtitles, add the `MYCOPSYCHOSIS.vtt` file to the `game/tl/{language}` folder.
  The subtitle feature supports all languages supported by the game.

<img src="README/Intro_Video_English.png" width="500">

### ~~2.2 Offline Website Feature (Korean Only - Canceled)~~

~~Implemented offline viewing of the in-game `mycopsychosis.online` website.~~

- ~~Added files (`game/webpage/`) (English, Spanish)~~
- ~~Added unofficial translation (Korean) version~~
- ~~Added Python-based local HTTP server (`game/webpage_host.py`) - video seeking, subtitle support (Korean only)~~
- ~~Removed due to copyright concerns with HTML files, OS and Python version dependency issues, and potential security risks with local hosting.~~

<img src="README/WebPage_Korean.png" width="500">

### ~~2.3 Unofficial Korean Translation~~

> Korean translation has been included in the official game update (v2.0, 2026.02.14) and is no longer needed as a patch.

<table>
  <tr>
    <td><img src="README/Title_Korean_Flag.png" width="500"></td>
    <td><img src="README/Preference_Korean.png" width="500"></td>
  </tr>
  <tr>
    <td><img src="README/Intro_Page_Korean.png" width="500"></td>
    <td><img src="README/LivingRoom_Korean.png" width="500"></td>
  </tr>
</table>

### ~~2.4 Bug Fixes (from Original Game)~~

Due to the change in patch's distribution method, this section has been temporarily removed from this patch.

- ~~**EndOnna Ending Image Partially Not Displayed**: Fixed issue where some Onna character images were not transitioning~~

> **Note:** The above bug fixes are unofficial minor fixes for very trivial bugs that do not affect gameplay, and have already been reported to DeltaCat Studio. These were discovered incidentally during the unofficial translation/patch work and included in this patch. There is no intention to criticize the quality of the original game.

---

## 3. File Structure

```
Patcher/
├── game/
│   ├── subtitle_standalone.rpy (Subtitle feature - no original file modification needed)
│   ├── MYCOPSYCHOSIS.vtt (Default subtitles - English)
│   └── tl/
│       └── korean/
│           └── MYCOPSYCHOSIS.vtt (Korean subtitles)
├── README.md (README-Main)
├── README_kor.md (README-Korean Version)
├── README_eng.md (README-English Version)
└── README/
    └── {Image Files for README files}
```

---

## 4. Disclaimer

- This patch is unofficial and is not affiliated with DeltaCat Studio.
- All copyrights for the game "Mycopsychosys Remastered" belong to DeltaCat Studio.
- This patch does not modify any original game files — it only provides additional files.
- If errors occur, you can restore the original state by deleting the added files (`subtitle_standalone.rpy`, `MYCOPSYCHOSIS.vtt`).
- This patch is provided without any warranty. The creator is not responsible for any errors, data corruption, or other issues caused by using this patch.

---

## 5. About the Game "Mycopsychosys: Remastered"

The game was developed by: [DeltaCatStudio](https://www.deltacatstudio.com/)

- [Mycopsychosys Remastered (Steam)](https://store.steampowered.com/app/3807550/Mycopsychosys_Remastered/)
- [Mycopsychosys Remastered (itch.io)](https://delta-cat-studio.itch.io/mycopsychosys)

Unofficial Patch developed by: [MuteJack](https://github.com/MuteJack/Mycopsychosys-UnOfficial-Patch)
