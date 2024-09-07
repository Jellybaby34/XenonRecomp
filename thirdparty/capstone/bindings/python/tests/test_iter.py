#!/usr/bin/env python3

# Capstone Python bindings, by Nguyen Anh Quynnh <aquynh@gmail.com>
from capstone import *
from xprint import to_hex


X86_CODE16 = b"\x8d\x4c\x32\x08\x01\xd8\x81\xc6\x34\x12\x00\x00"
X86_CODE32 = b"\xba\xcd\xab\x00\x00\x8d\x4c\x32\x08\x01\xd8\x81\xc6\x34\x12\x00\x00"
X86_CODE64 = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"
ARM_CODE = b"\xED\xFF\xFF\xEB\x04\xe0\x2d\xe5\x00\x00\x00\x00\xe0\x83\x22\xe5\xf1\x02\x03\x0e\x00\x00\xa0\xe3\x02\x30\xc1\xe7\x00\x00\x53\xe3"
ARM_CODE2 = b"\x10\xf1\x10\xe7\x11\xf2\x31\xe7\xdc\xa1\x2e\xf3\xe8\x4e\x62\xf3"
THUMB_CODE = b"\x70\x47\xeb\x46\x83\xb0\xc9\x68"
THUMB_CODE2 = b"\x4f\xf0\x00\x01\xbd\xe8\x00\x88\xd1\xe8\x00\xf0"
THUMB_MCLASS = b"\xef\xf3\x02\x80"
ARMV8 = b"\xe0\x3b\xb2\xee\x42\x00\x01\xe1\x51\xf0\x7f\xf5"
MIPS_CODE = b"\x0C\x10\x00\x97\x00\x00\x00\x00\x24\x02\x00\x0c\x8f\xa2\x00\x00\x34\x21\x34\x56"
MIPS_CODE2 = b"\x56\x34\x21\x34\xc2\x17\x01\x00"
MIPS_32R6M = b"\x00\x07\x00\x07\x00\x11\x93\x7c\x01\x8c\x8b\x7c\x00\xc7\x48\xd0"
MIPS_32R6 = b"\xec\x80\x00\x19\x7c\x43\x22\xa0"
AARCH64_CODE = b"\x21\x7c\x02\x9b\x21\x7c\x00\x53\x00\x40\x21\x4b\xe1\x0b\x40\xb9"
PPC_CODE = b"\x80\x20\x00\x00\x80\x3f\x00\x00\x10\x43\x23\x0e\xd0\x44\x00\x80\x4c\x43\x22\x02\x2d\x03\x00\x80\x7c\x43\x20\x14\x7c\x43\x20\x93\x4f\x20\x00\x21\x4c\xc8\x00\x21"
PPC_CODE2 = b"\x10\x60\x2a\x10\x10\x64\x28\x88\x7c\x4a\x5d\x0f"
SPARC_CODE = b"\x80\xa0\x40\x02\x85\xc2\x60\x08\x85\xe8\x20\x01\x81\xe8\x00\x00\x90\x10\x20\x01\xd5\xf6\x10\x16\x21\x00\x00\x0a\x86\x00\x40\x02\x01\x00\x00\x00\x12\xbf\xff\xff\x10\xbf\xff\xff\xa0\x02\x00\x09\x0d\xbf\xff\xff\xd4\x20\x60\x00\xd4\x4e\x00\x16\x2a\xc2\x80\x03"
SPARCV9_CODE = b"\x81\xa8\x0a\x24\x89\xa0\x10\x20\x89\xa0\x1a\x60\x89\xa0\x00\xe0"
SYSZ_CODE = b"\xed\x00\x00\x00\x00\x1a\x5a\x0f\x1f\xff\xc2\x09\x80\x00\x00\x00\x07\xf7\xeb\x2a\xff\xff\x7f\x57\xe3\x01\xff\xff\x7f\x57\xeb\x00\xf0\x00\x00\x24\xb2\x4f\x00\x78"
XCORE_CODE = b"\xfe\x0f\xfe\x17\x13\x17\xc6\xfe\xec\x17\x97\xf8\xec\x4f\x1f\xfd\xec\x37\x07\xf2\x45\x5b\xf9\xfa\x02\x06\x1b\x10"
M68K_CODE = b"\xd4\x40\x87\x5a\x4e\x71\x02\xb4\xc0\xde\xc0\xde\x5c\x00\x1d\x80\x71\x12\x01\x23\xf2\x3c\x44\x22\x40\x49\x0e\x56\x54\xc5\xf2\x3c\x44\x00\x44\x7a\x00\x00\xf2\x00\x0a\x28\x4E\xB9\x00\x00\x00\x12\x4E\x75"
M680X_CODE = b"\x06\x10\x19\x1a\x55\x1e\x01\x23\xe9\x31\x06\x34\x55\xa6\x81\xa7\x89\x7f\xff\xa6\x9d\x10\x00\xa7\x91\xa6\x9f\x10\x00\x11\xac\x99\x10\x00\x39"
ALPHA_CODE = b'\x02\x00\xbb\x27\x50\x7a\xbd\x23\xd0\xff\xde\x23\x00\x00\x5e\xb7'
ALPHA_CODE_BE = b'\x27\xbb\x00\x02\x23\xbd\x7a\x50\x23\xde\xff\xd0\xb7\x5e\x00\x00'
HPPA_20_CODE_BE = b'\x00\x20\x50\xa2\x00\x01\x58\x20\x00\x00\x44\xa1\x00\x41\x18\x40\x00\x20\x08\xa2\x01\x60\x48\xa1\x01\x61\x18\xc0\x00\x00\x14\xa1\x00\x0f\x0d\x61\x00\x0f\x0e\x61\x00\x01\x18\x60\x00\x00\x0c\x00\x00\x00\x0c\xa0\x03\xff\xc0\x1f\x00\x00\x04\x00\x00\x10\x04\x00\x04\x22\x51\x83\x04\x22\x51\xc3\x04\x22\x51\x83\x04\x2f\x71\x83\x04\x2f\x71\xc3\x04\x2f\x71\x83\x04\x41\x53\x43\x04\x41\x53\x63\x04\x41\x53\x03\x04\x41\x12\x00\x04\x41\x16\x00\x04\x41\x16\x20\x04\x41\x42\x00\x04\x41\x46\x00\x04\x41\x46\x20\x04\x41\x12\x40\x04\x41\x12\x60\x04\x41\x42\x40\x04\x41\x42\x60\x04\x41\x18\x00\x04\x41\x08\x00\x04\x41\x13\x80\x04\x41\x13\xa0\x04\x41\x52\x80\x04\x41\x52\xa0\x04\x5e\x72\x80\x04\x41\x42\x80\x04\x41\x52\xc0\x04\x41\x52\xe0\x04\x41\x42\xc0\x04\x41\x42\xe0\x14\x00\xde\xad'
HPPA_20_CODE =    b'\xa2\x50\x20\x00\x20\x58\x01\x00\xa1\x44\x00\x00\x40\x18\x41\x00\xa2\x08\x20\x00\xa1\x48\x60\x01\xc0\x18\x61\x01\xa1\x14\x00\x00\x61\x0d\x0f\x00\x61\x0e\x0f\x00\x60\x18\x01\x00\x00\x0c\x00\x00\xa0\x0c\x00\x00\x1f\xc0\xff\x03\x00\x04\x00\x00\x00\x04\x10\x00\x83\x51\x22\x04\xc3\x51\x22\x04\x83\x51\x22\x04\x83\x71\x2f\x04\xc3\x71\x2f\x04\x83\x71\x2f\x04\x43\x53\x41\x04\x63\x53\x41\x04\x03\x53\x41\x04\x00\x12\x41\x04\x00\x16\x41\x04\x20\x16\x41\x04\x00\x42\x41\x04\x00\x46\x41\x04\x20\x46\x41\x04\x40\x12\x41\x04\x60\x12\x41\x04\x40\x42\x41\x04\x60\x42\x41\x04\x00\x18\x41\x04\x00\x08\x41\x04\x80\x13\x41\x04\xa0\x13\x41\x04\x80\x52\x41\x04\xa0\x52\x41\x04\x80\x72\x5e\x04\x80\x42\x41\x04\xc0\x52\x41\x04\xe0\x52\x41\x04\xc0\x42\x41\x04\xe0\x42\x41\x04\xad\xde\x00\x14'
HPPA_11_CODE_BE = b'\x24\x41\x40\xc3\x24\x41\x60\xc3\x24\x41\x40\xe3\x24\x41\x60\xe3\x24\x41\x68\xe3\x2c\x41\x40\xc3\x2c\x41\x60\xc3\x2c\x41\x40\xe3\x2c\x41\x60\xe3\x2c\x41\x68\xe3\x24\x62\x42\xc1\x24\x62\x62\xc1\x24\x62\x42\xe1\x24\x62\x46\xe1\x24\x62\x62\xe1\x24\x62\x6a\xe1\x2c\x62\x42\xc1\x2c\x62\x62\xc1\x2c\x62\x42\xe1\x2c\x62\x46\xe1\x2c\x62\x62\xe1\x2c\x62\x6a\xe1\x24\x3e\x50\xc2\x24\x3e\x50\xe2\x24\x3e\x70\xe2\x24\x3e\x78\xe2\x2c\x3e\x50\xc2\x2c\x3e\x50\xe2\x2c\x3e\x70\xe2\x2c\x3e\x78\xe2\x24\x5e\x52\xc1\x24\x5e\x52\xe1\x24\x5e\x56\xe1\x24\x5e\x72\xe1\x24\x5e\x7a\xe1\x2c\x5e\x52\xc1\x2c\x5e\x52\xe1\x2c\x5e\x56\xe1\x2c\x5e\x72\xe1\x2c\x5e\x7a\xe1'
HPPA_11_CODE =    b'\xc3\x40\x41\x24\xc3\x60\x41\x24\xe3\x40\x41\x24\xe3\x60\x41\x24\xe3\x68\x41\x24\xc3\x40\x41\x2c\xc3\x60\x41\x2c\xe3\x40\x41\x2c\xe3\x60\x41\x2c\xe3\x68\x41\x2c\xc1\x42\x62\x24\xc1\x62\x62\x24\xe1\x42\x62\x24\xe1\x46\x62\x24\xe1\x62\x62\x24\xe1\x6a\x62\x24\xc1\x42\x62\x2c\xc1\x62\x62\x2c\xe1\x42\x62\x2c\xe1\x46\x62\x2c\xe1\x62\x62\x2c\xe1\x6a\x62\x2c\xc2\x50\x3e\x24\xe2\x50\x3e\x24\xe2\x70\x3e\x24\xe2\x78\x3e\x24\xc2\x50\x3e\x2c\xe2\x50\x3e\x2c\xe2\x70\x3e\x2c\xe2\x78\x3e\x2c\xc1\x52\x5e\x24\xe1\x52\x5e\x24\xe1\x56\x5e\x24\xe1\x72\x5e\x24\xe1\x7a\x5e\x24\xc1\x52\x5e\x2c\xe1\x52\x5e\x2c\xe1\x56\x5e\x2c\xe1\x72\x5e\x2c\xe1\x7a\x5e\x2c'

all_tests = (
        (CS_ARCH_X86, CS_MODE_16, X86_CODE16, "X86 16bit (Intel syntax)", None),
        (CS_ARCH_X86, CS_MODE_32, X86_CODE32, "X86 32bit (ATT syntax)", CS_OPT_SYNTAX_ATT),
        (CS_ARCH_X86, CS_MODE_32, X86_CODE32, "X86 32 (Intel syntax)", None),
        (CS_ARCH_X86, CS_MODE_32, X86_CODE32, "X86 32 (MASM syntax)", CS_OPT_SYNTAX_MASM),
        (CS_ARCH_X86, CS_MODE_64, X86_CODE64, "X86 64 (Intel syntax)", None),
        (CS_ARCH_ARM, CS_MODE_ARM, ARM_CODE, "ARM", None),
        (CS_ARCH_ARM, CS_MODE_THUMB, THUMB_CODE2, "THUMB-2", None),
        (CS_ARCH_ARM, CS_MODE_ARM, ARM_CODE2, "ARM: Cortex-A15 + NEON", None),
        (CS_ARCH_ARM, CS_MODE_THUMB, THUMB_CODE, "THUMB", None),
        (CS_ARCH_ARM, CS_MODE_THUMB + CS_MODE_MCLASS, THUMB_MCLASS, "Thumb-MClass", None),
        (CS_ARCH_ARM, CS_MODE_ARM + CS_MODE_V8, ARMV8, "Arm-V8", None),
        (CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_BIG_ENDIAN, MIPS_CODE, "MIPS-32 (Big-endian)", None),
        (CS_ARCH_MIPS, CS_MODE_MIPS64 + CS_MODE_LITTLE_ENDIAN, MIPS_CODE2, "MIPS-64-EL (Little-endian)", None),
        (CS_ARCH_MIPS, CS_MODE_MIPS32R6 + CS_MODE_MICRO + CS_MODE_BIG_ENDIAN, MIPS_32R6M, "MIPS-32R6 | Micro (Big-endian)", None),
        (CS_ARCH_MIPS, CS_MODE_MIPS32R6 + CS_MODE_BIG_ENDIAN, MIPS_32R6, "MIPS-32R6 (Big-endian)", None),
        (CS_ARCH_AARCH64, CS_MODE_ARM, AARCH64_CODE, "AARCH64", None),
        (CS_ARCH_PPC, CS_MODE_BIG_ENDIAN, PPC_CODE, "PPC-64", None),
        (CS_ARCH_PPC, CS_MODE_BIG_ENDIAN, PPC_CODE, "PPC-64, print register with number only", CS_OPT_SYNTAX_NOREGNAME),
        (CS_ARCH_PPC, CS_MODE_BIG_ENDIAN + CS_MODE_QPX, PPC_CODE2, "PPC-64 + QPX", CS_OPT_SYNTAX_NOREGNAME),
        (CS_ARCH_SPARC, CS_MODE_BIG_ENDIAN, SPARC_CODE, "Sparc", None),
        (CS_ARCH_SPARC, CS_MODE_BIG_ENDIAN + CS_MODE_V9, SPARCV9_CODE, "SparcV9", None),
        (CS_ARCH_SYSZ, 0, SYSZ_CODE, "SystemZ", None),
        (CS_ARCH_XCORE, 0, XCORE_CODE, "XCore", None),
        (CS_ARCH_M68K, CS_MODE_BIG_ENDIAN | CS_MODE_M68K_040, M68K_CODE, "M68K (68040)", None),
        (CS_ARCH_M680X, CS_MODE_M680X_6809, M680X_CODE, "M680X_M6809", None),
        (CS_ARCH_ALPHA, CS_MODE_LITTLE_ENDIAN, ALPHA_CODE, "Alpha (Little-endian)", None),
        (CS_ARCH_ALPHA, CS_MODE_BIG_ENDIAN, ALPHA_CODE_BE, "Alpha (Big-endian)", None),
        (CS_ARCH_HPPA, CS_MODE_BIG_ENDIAN | CS_MODE_HPPA_20, HPPA_20_CODE_BE, "HPPA 2.0 (Big-endian)", None),
        (CS_ARCH_HPPA, CS_MODE_LITTLE_ENDIAN | CS_MODE_HPPA_20, HPPA_20_CODE, "HPPA 2.0 (Little-endian)", None),
        (CS_ARCH_HPPA, CS_MODE_BIG_ENDIAN | CS_MODE_HPPA_11, HPPA_11_CODE_BE, "HPPA 1.1 (Big-endian)", None),
        (CS_ARCH_HPPA, CS_MODE_LITTLE_ENDIAN | CS_MODE_HPPA_11, HPPA_11_CODE, "HPPA 1.1 (Little-endian)", None),
        )

# ## Test class Cs
def test_class():
    for (arch, mode, code, comment, syntax) in all_tests:
        print('*' * 16)
        print("Platform: %s" % comment)
        print("Code: %s" % to_hex(code))
        print("Disasm:")

        try:
            md = Cs(arch, mode)

            if syntax is not None:
                md.syntax = syntax

            for (addr, size, mnemonic, op_str) in md.disasm_iter(code, 0x1000):
                print("0x%x:\t%s\t%s" % (addr, mnemonic, op_str))

            print("0x%x:" % (addr + size))
            print()
        except CsError as e:
            print("ERROR: %s" % e)

if __name__ == '__main__':
    test_class()
