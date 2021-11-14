#!/usr/bin/python3

# No longer necessary with release v2.0.
#
# This script corrects invalid RVAs by rebasing the .idb to WoW's imagebase.
# See plugin output:
#   [WoWDumpFix] IDA Pro Info:
#   [WoWDumpFix] WoW base address = 000000013F790000


import idc
import idaapi


def main():
    wow_imagebase = idc.AskAddr(idc.BADADDR, "Enter WoW's base address.")
    if wow_imagebase and wow_imagebase is not idc.BADADDR:
        delta = wow_imagebase - idaapi.get_imagebase()
        status = rebase_program(delta, idc.MSF_NOFIX)
        if status is not idc.MOVE_SEGM_OK:
            print "rebase_program failed %d." % (status)


if __name__ == '__main__':
    main()