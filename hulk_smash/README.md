# Hulk Smash

## Binary Exploitation - 100 points

### Introduction

Hulk Smash is one of the most well-designed challenges for people new to binary exploitation in capture-the-flag competitions. My peers and co-workers who were first-time competitors in Cyberstakes would ask me "Where do I begin? How do I learn binary exploitation?". I recommended that they spend the remaining days left in the competition solving Hulk Smash. It is a beginner to intermediate level binary exploitation problem that does a great job of providing enough complexity to simulate real-world binary protocols, but simple enough to teach the fundamentals of binary exploitation such as stack-based buffer overflows to gain control of EIP and execute shellcode.

## First Steps

Like any binary exploitation problem, the first step should always be running `checksec` to see which security features are enabled. Given that this is a beginner challenge, all security features such as address space layout randomization (ASLR), stack canaries, and non-executable stack are turned off. Below is the output of the command: 

TODO: PUT SCREENSHOT HERE

Next, let's open the binary in a static dissassembler. I prefer Binary Ninja. 