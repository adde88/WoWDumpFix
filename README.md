# World of Warcraft Dump Fix

## Summary

**This is a modified version of: Overwatch-Dump-Fix which was made by changeofpace**  
This x64dbg plugin removes anti-dumping and obfuscation techniques from the popular MMORPG game World of Warcraft. It is meant to be used with Scylla (built into x64dbg) to produce process dump files for static analysis.

This project is for educational use only.

## Release v5.0.1 (5.23.2017)

- The import address table is no longer terminated by two null pointers. The second null has been replaced with a pointer to a 'ret 0' instruction.

## Usage

### Added commands

- **WoWDumpFix**

### x64dbg

1. Attach x64dbg to WoW-64.exe then execute the **WoWDumpFix** command.
2. Open **Scylla** in x64dbg's **Plugins** menu then select WoW-64.exe in the "Attach to an active process" drop-down list.
3. Click **IAT Autosearch** -> **Get Imports**.
4. Click **Dump** to create a dump file.
5. Click **Fix Dump** and select the dump file from (4) to reconstruct imports.
6. The Scylla output view should say "Import Rebuild success [FILE PATH]".
7. Click **PE Rebuild** and select the fixed dump file.

### IDA Pro

8. Open the dump file in IDA. Check the **Manual load** and **Load resources** (optional) boxes.  Click **OK** / **Yes** for every prompt.
9. Run the **Universal Unpacker Manual Reconstruct** plugin for the IAT to set imports to the correct color.
10. Happy reversing :sunglasses:.

## Building

A post-build event requires the **"X96DBG_PATH"** environment variable to be defined to x64dbg's installation directory.

## Notes

- This plugin is tested while offline on battle.net.
