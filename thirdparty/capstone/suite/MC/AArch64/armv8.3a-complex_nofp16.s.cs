# CS_ARCH_AARCH64, 0, None

0x20,0xc4,0x82,0x2e == fcmla	v0.2s, v1.2s, v2.2s, #0
0x20,0xc4,0x82,0x6e == fcmla	v0.4s, v1.4s, v2.4s, #0
0x20,0xc4,0xc2,0x6e == fcmla	v0.2d, v1.2d, v2.2d, #0
0x20,0xc4,0x82,0x2e == fcmla	v0.2s, v1.2s, v2.2s, #0
0x20,0xcc,0x82,0x2e == fcmla	v0.2s, v1.2s, v2.2s, #90
0x20,0xd4,0x82,0x2e == fcmla	v0.2s, v1.2s, v2.2s, #180
0x20,0xdc,0x82,0x2e == fcmla	v0.2s, v1.2s, v2.2s, #270
0x20,0xe4,0x82,0x2e == fcadd	v0.2s, v1.2s, v2.2s, #90
0x20,0xe4,0x82,0x6e == fcadd	v0.4s, v1.4s, v2.4s, #90
0x20,0xe4,0xc2,0x6e == fcadd	v0.2d, v1.2d, v2.2d, #90
0x20,0xe4,0x82,0x2e == fcadd	v0.2s, v1.2s, v2.2s, #90
0x20,0xf4,0x82,0x2e == fcadd	v0.2s, v1.2s, v2.2s, #270
0x20,0x10,0x82,0x6f == fcmla	v0.4s, v1.4s, v2.s[0], #0
0x20,0x30,0x82,0x6f == fcmla	v0.4s, v1.4s, v2.s[0], #90
0x20,0x50,0x82,0x6f == fcmla	v0.4s, v1.4s, v2.s[0], #180
0x20,0x70,0x82,0x6f == fcmla	v0.4s, v1.4s, v2.s[0], #270
0x20,0x18,0x82,0x6f == fcmla	v0.4s, v1.4s, v2.s[1], #0
