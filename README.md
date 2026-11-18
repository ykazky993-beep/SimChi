# KimChi — Simple Chipped (SimChi)

Copyright © 2026 ykazky993-beep.

Licensed under the [MIT License](LICENSE).

---

## 1. Introduction

**KimChi (Simple Chipped)** is a lightweight character transformation and encoding project developed using Python.

KimChi uses simple mathematical operations to transform characters into numerical representations. Each character is mapped to an index based on a predefined character table, then processed using a numerical parameter called `coder`.

The project consists of multiple variants, each implementing a different mathematical transformation.

KimChi prioritizes:
- Simple mathematical operations.
- Lightweight implementation.
- Configurable parameters.
- Independent encoding and decoding processes.
- Minimal dependencies.
- Freedom for users to determine their own parameters.

KimChi is designed as a simple encoding and character transformation system, not as a cryptographically secure encryption algorithm.

## 2. Core Concept

The fundamental mechanism behind KimChi is **Character Mapping**.

KimChi does not directly transform characters into arbitrary numerical values. Instead, each character is first assigned an index based on the `CHARACTERS` variable defined in `config.py`.

For example, assuming the character table contains:

    CHARACTERS = "ABCDE"

The mapping becomes:

| Character | Index |
|---|---:|
| A | 0 |
| B | 1 |
| C | 2 |
| D | 3 |
| E | 4 |

The index starts from zero because Python uses zero-based indexing.

When a user enters a character, KimChi searches for its position in the character table.

For example:

    Input: CAB

The mapping process produces:

    C = 2
    A = 0
    B = 1

The resulting numerical sequence is:

    2,0,1

These indices are subsequently processed using the mathematical transformation of the selected KimChi variant.

**Important:** The actual supported characters depend entirely on the contents of `CHARACTERS` in `config.py`.

## 3. The Coder Parameter

The `coder` is a numerical parameter used during character transformation.

Depending on the selected variant, the coder acts as:
- A multiplication factor.
- An exponent.
- A parameter used in multiple mathematical operations.

The coder must be supplied during decoding because the decoder needs the same parameter to reverse the transformation.

### Coder recommendations

KimChi does not impose a mandatory upper limit on coder values in the variants designed for unrestricted input.

However, the developer provides recommended values for normal usage.

Values outside the recommended range may still be accepted, but users should understand the potential computational consequences.

Large coder values can produce extremely large integers, increasing processing time and memory consumption.

The responsibility for choosing coder values outside the recommendations belongs to the user.

## 4. Mathematical Transformation

KimChi currently has multiple variants with different mathematical approaches.

The following explanations describe the transformation applied to each character.

Let:

- `p` = character index.
- `c` = coder.
- `v` = transformed numerical value.

### Usage

installation and usage:

    git clone https://github.com/ykazky993-beep/SimChi.git
    cd SimChi/SimChi/KimChi
    python3 -m KCV32.kcv32
    python3 -m KCV64.kcv64
    python3 -m KCV96.kcv96
    python3 -m KCV192.kcv192

Avoid using `python3 kcvxxx.py` utils can be not detected.

### KCV32 — Multiplication

KCV32 uses basic multiplication.

Formula:

    v = p × c

Example:

    Character index = 5
    Coder = 3

    v = 5 × 3
    v = 15

The resulting value is:

    15

During decoding, the process is reversed using integer division:

    p = v ÷ c

The decoder also checks whether the numerical value is divisible by the supplied coder.

If the remainder is not zero, the input is rejected.

KCV32 also provides an optional Base32 representation of the numerical sequence.

### KCV64 — Exponentiation

KCV64 uses exponentiation instead of multiplication.

Formula:

    v = p^c

Example:

    Character index = 5
    Coder = 3

    v = 5³
    v = 125

The resulting value is:

    125

During decoding, the decoder calculates the corresponding integer root:

    p = ⁿ√v

Where `n` represents the coder.

The decoder then verifies the result by checking:

    p^c == v

This validation ensures that the supplied numerical value is an exact power rather than an approximate mathematical result.

KCV64 uses the coder as an exponent, meaning larger values can significantly increase the resulting numerical representation.

### KCV96 — Multiplication with Dual Base Encoding

KCV96 uses the same mathematical transformation as KCV32.

Formula:

    v = p × c

However, KCV96 introduces an additional representation layer.

Its encoding process consists of:

1. Character mapping.
2. Multiplication using the coder.
3. Joining numerical values using commas.
4. Base32 encoding.
5. Base64 encoding of the Base32 result.

The representation process can be expressed as:

    Numerical Sequence
          |
        Base32
          |
        Base64
          |
       BASEDUAL

During decoding, the reverse representation process is performed:

    BASEDUAL
       |
     Base64 Decode
       |
     Base32 Decode
       |
    Numerical Sequence
       |
    Mathematical Decoding

The `is_b64` utility is used by the decoder to determine whether the supplied data needs the additional decoding steps.

### KCV192 — Multiplication and Exponentiation

KCV192 combines multiplication and exponentiation into a single transformation.

Unlike KCV32 and KCV96, it uses the coder in two mathematical operations.

First:

    r1 = p × c

Then:

    v = r1^c

Combined formula:

    v = (p × c)^c

Example:

    Character index = 5
    Coder = 3

    r1 = 5 × 3
    r1 = 15

    v = 15³
    v = 3375

The resulting value is:

    3375

During decoding, KCV192 reverses the transformation in two stages.

**Stage 1 — Integer Root**

The decoder calculates the exact integer root:

    r1 = ⁿ√v

KCV192 implements an `integer_root()` function using binary search.

This approach searches for an integer whose power equals the supplied numerical value.

If no exact integer root exists, the decoder rejects the input.

**Stage 2 — Reverse Multiplication**

After obtaining `r1`, the decoder checks whether it is divisible by the coder.

Then:

    p = r1 ÷ c

Finally, the resulting position is checked against the character table.

This allows KCV192 to reverse its combined mathematical transformation.

## 5. Encoding Process

Although every variant uses a different mathematical transformation, their general encoding architecture follows a similar structure.

    User Input
        |
        v
    Character Validation
        |
        v
    Character Mapping
        |
        v
    Mathematical Transformation
        |
        v
    Numerical Sequence
        |
        v
    Optional Representation Layer
        |
        v
    Encoded Output

### Character Validation

Before transformation, every character is checked against `CHARACTERS`.

If a character does not exist in the character table, the program reports an unsupported character error.

### Mathematical Transformation

Each character is independently transformed into a numerical value.

The resulting values are stored in a list.

### Joining

After transformation, the numerical values are converted into strings and joined using commas.

Example:

    15,0,21,9,12

The comma separator allows the decoder to distinguish individual numerical values.

### Additional Representation

Depending on the variant, the numerical sequence may be represented using Base32 or Base64.

These representations do not replace the mathematical transformation. They are additional encoding layers.

## 6. Decoding Process

Decoding reverses the operations performed during encoding.

General architecture:

    Encoded Input
        |
        v
    Representation Decoding
        |
        v
    Numerical Sequence
        |
        v
    Mathematical Reversal
        |
        v
    Character Index
        |
        v
    Character Mapping
        |
        v
    Decoded Output

Each numerical value is processed independently.

The decoder performs several validation steps:

1. Validate the coder.
2. Parse numerical values.
3. Reverse the mathematical transformation.
4. Validate the resulting character index.
5. Retrieve the corresponding character from `CHARACTERS`.

If an invalid value is encountered, the decoder reports an error instead of returning an invalid character.

## 7. Variant Comparison

| Variant | Mathematical Operation | Additional Encoding |
|---|---|---|
| KCV32 | Multiplication | Optional Base32 |
| KCV64 | Exponentiation | None |
| KCV96 | Multiplication | Base32 + Base64 |
| KCV192 | Multiplication + Exponentiation | Base64 |
| KCV256 | Under Development | TBD |
| KCV512 | Under Development | TBD |

KCV256 and KCV512 are currently under development. Their mechanisms and specifications have not yet been finalized.

## 8. Base32 and Base64

KimChi uses standard Python Base64 library functions for additional data representation.

These functions include:

- `base64.b32encode()`
- `base64.b32decode()`
- `base64.b64encode()`
- `base64.b64decode()`

Base32 and Base64 are encoding formats, not encryption algorithms.

Their purpose in KimChi is to provide alternative representations of the numerical sequence.

### KCV32 Base32 Utility

KCV32 provides a Base32 output as an optional representation.

The primary numerical output is identified by:

    CODE:

The Base32 representation is identified by:

    BASE32:

To recover the numerical sequence from the Base32 representation, users can use the separate utility:

    dbase32.py

The resulting numerical sequence can then be supplied to the KCV32 decoder.

### KCV96 Dual Representation

KCV96 uses two representation layers:

    Numerical Sequence
          |
        Base32
          |
        Base64

The resulting `BASEDUAL` can be passed to its decoder, which reverses both representation layers before performing mathematical decoding.

## 9. Error Handling and Validation

KimChi implements basic validation to prevent invalid input from being processed.

Common validation cases include:

| Error | Description |
|---|---|
| Unsupported Character | Character is not present in `CHARACTERS`. |
| Invalid Coder | Coder is not a valid positive integer. |
| Invalid Data | Input cannot be parsed into valid numerical values. |
| Invalid Character | Recovered index is outside the character table. |
| Invalid Root | Numerical value does not have an exact integer root. |
| Invalid Base64 | Supplied Base64 representation cannot be decoded. |

The decoder also checks mathematical consistency.

For example, KCV32 checks divisibility, KCV64 checks exact exponentiation, and KCV192 checks both exact integer roots and divisibility.

These checks help detect malformed or incompatible input. They do not provide cryptographic integrity verification.

## 10. Limitations

KimChi is intentionally built around simple mathematical operations.

Users should understand the following limitations:

- The character table determines which characters can be processed.
- Encoding and decoding require compatible character tables.
- The correct coder must be supplied during decoding.
- Incorrect coder values can produce invalid decoding results.
- Large exponents can generate extremely large integers.
- Base32 and Base64 do not provide data confidentiality.
- The mathematical transformations are reversible and should not be considered cryptographically secure.

KimChi does not currently implement cryptographic authentication, integrity protection, or secure key management.

**Do not use KimChi as a replacement for established cryptographic systems when protecting sensitive information.**

## 11. Development Philosophy

KimChi follows a lightweight development philosophy.

Its primary objective is to demonstrate how simple mathematical operations and character indexing can be combined into multiple encoding and decoding mechanisms.

The project avoids unnecessary complexity and mandatory parameter restrictions.

Developer recommendations are provided as guidance rather than universal guarantees.

Users retain control over their parameters and should understand the computational consequences of their choices.

## 12. Project Status

| Variant | Development Status |
|---|---|
| KCV32 | Available |
| KCV64 | Available |
| KCV96 | Available |
| KCV192 | Available |
| KCV256 | Under Development |
| KCV512 | Under Development |

Future development may introduce additional variants, utilities, and improvements to the existing implementation.

---

Copyright © 2026 ykazky993-beep.

Licensed under the [MIT License](LICENSE).
