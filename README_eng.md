# Mycopsychosys Remastered - Unofficial Feature/Korean Translation Patch

> NOTE: If you want to read this in Korean, check [README_kor.md](README_kor.md)

Unofficial feature patch for Mycopsychosys Remastered.
Including useful features (ex: subtitle for intro video) and Korean translation.
Note that this patch may not work if the game is updated.

---

## 0. Information

### 0.1. Version Info

- Game: Mycopsychosys Remastered
- Game Version: Mycopsychosys v2.0 (2026.01.06)
- Patch Version: 1.0.5 (2026.02.07)

### 0.2. Environment Support (For Automatic Patcher)

- O/S: Windows 10 or Later
- Game Platform: Steam (Not tested with the game purchased/downloaded from Itch.io.)

---

## 1. Installation

1. Purchase and install Mycopsychosys Remastered from Steam.
2. Copy the Patcher folder into the game installation folder.
   1. Default path: `C:\Program Files (x86)\Steam\steamapps\common\Mycopsychosys Remastered\`
   2. Other path: `{Drive Letter}:\SteamLibrary\steamapps\common\Mycopsychosys Remastered\`
3. Download `Git for Windows/x64 Portable` from the [git website](https://git-scm.com/install/windows) and extract it into the `\PortableGit` folder inside the Patcher folder.
   Can download from:  `https://git-scm.com/install/windows`
4. Run `apply_patch.bat` in the Patcher folder.
5. Launch the game and verify the added features and languages (Korean).

---

## 2. Additional Features / Changes

### 2.1 Intro Video Subtitle System (Subtitle Files and Feature)

Displays subtitles on the intro video in-game.

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
- ~~Added Subtitle for Video~~
- ~~Added Python-based local HTTP server (`game/webpage_host.py`) - video seeking, subtitle support (Korean only)~~
- ~~Removed due to copyright concerns with HTML files, OS and Python version dependency issues, and potential security risks with local hosting.~~

<img src="README/WebPage_Korean.png" width="500">

### 2.3. Unofficial Korean Translation Added

#### 2.3.1 Korean Option Added to Preference > Language

- Rather than overwriting other languages (translations), new options have been added.
- Therefore, the addition of the Korean translation will not affect other languages.

<table>
  <tr>
    <td><img src="README/Title_Korean_Flag.png" width="500"></td>
    <td><img src="README/Preference_Korean.png" width="500"></td>
  </tr>
</table>

#### 2.3.2 Korean Translation (Scripts)

- Full game text translation (`game/tl/korean/`)
- Character name translation
- UI/Menu translation
- Korean font (NanumGothic) added

<img src="README/Intro_Page_Korean.png" width="500">

#### 2.3.3 Korean UI Button Images

- In-Game: Basement, Bathroom, Bedroom, FrontDoor, Hallway, Kitchen, LivingRoom, Loft, Window
- Game Intro: Skip buttons

<img src="README/LivingRoom_Korean.png" width="500">

### 2.4 Bug Fixes (from Original Game)

#### 2.4.1 Original Game Bug Fixes

- **EndOnna Ending Image Partially Not Displayed**: Fixed issue where some Onna character images were not transitioning
- **Bedroom PC Selection Script Translation Not Applied (Korean Only)**: Added branch point to original script due to missing Ren'Py translation hash for PC selection. Further fixes planned.

> **Note:** The above bug fixes are unofficial minor fixes for very trivial bugs that do not affect gameplay, and have already been reported to DeltaCat Studio. These were discovered incidentally during the unofficial translation/patch work and included in this patch. There is no intention to criticize the quality of the original game.

#### 2.4.2 Credits Fix

- Separated French/Russian translator info lines (fixed underline not applying to language names)
- Added Korean translator (MuteJack, Unofficial)

### ~~2.5 Additional Development Tools for Translation (Removed)~~

- ~~`check_apostrophe.py`: Auto-detection tool for apostrophe inconsistencies in translation files. The game uses mixed straight(') and curly(') apostrophes.~~

---

## 3. File Structure

```
Patcher/
├── apply_patch.bat (Script File for Apply this Patch)
├── unofficial_patch_{updated_date}.dat
├── PortableGit/
|   └── PortableGit-2.52.0-64-bit.7z.exe (Download from git website required)
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
- The patch file does not contain any original game scripts or resource files. It only includes a data file with minimal modification history, along with the batch script and file structure needed to apply it to the game.
  - The development repository contains numerous original game files/scripts. To protect copyright, only the patch file is distributed instead of the modified files.
  - For this reason, the development repository is not public. Requests to release the repository/source code (including private messages) will not be accepted.
  - The patch creator respects DeltaCat Studio and their works, and has no intention of infringing on the rights of the original game.
- The target version for this patch is **Mycopsychosys Remastered v2.0 (2026.01.26 Update)**. If the game is updated, the patch may not be applied correctly or may cause unexpected problems.
- If errors occur, you can restore the original state by deleting the game folder and reinstalling.
  - Due to the nature of Steam games, modifications will not be removed during reinstallation unless the game folder is deleted first.
- This patch is provided without any warranty. The creator is not responsible for any errors, data corruption, or other issues caused by using this patch.

---

## 5. About the Game "Mycopsychosys: Remastered"

The game was developed by: [DeltaCatStudio](https://www.deltacatstudio.com/)

- [Mycopsychosys Remastered (Steam)](https://store.steampowered.com/app/3807550/Mycopsychosys_Remastered/)
- [Mycopsychosys Remastered (itch.io)](https://delta-cat-studio.itch.io/mycopsychosys)

Unofficial Patch developed by: [MuteJack](https://github.com/MuteJack/Mycopsychosys-UnOfficial-Patch)
