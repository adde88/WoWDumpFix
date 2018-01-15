# No longer necessary with release v2.0.
#
# This script corrects invalid RVAs by rebasing the .idb to World of Warcraft's imagebase.
# See plugin output:
#   [World of Warcraft Dump Fix] IDA Pro Info:
#   [World of Warcraft Dump Fix]     wow base address = 000000013F790000


import idc
import idaapi


def main():
    wow_imagebase = idc.AskAddr(idc.BADADDR, "Enter WoW-64.exe's base address.")
    if wow_imagebase and wow_imagebase is not idc.BADADDR:
        delta = wow_imagebase - idaapi.get_imagebase()
        status = rebase_program(delta, idc.MSF_NOFIX)
        if status is not idc.MOVE_SEGM_OK:
            print "rebase_program failed %d." % (status)


if __name__ == '__main__':
    main()