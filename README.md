# A key-value database (For miniLCTF 2022)

A CTF challenge for miniLCTF 2022：[Repo](https://github.com/XDSEC/miniLCTF_2022/tree/main/Challenges/kvdb)

> Easy key-value database written in `C/C++` language.

# Doc

## 0x00 Opcodes

- `ADD`: Add a new kvpair to database.
- `DEL`: Delete a kvpair fromm database by `key`.
- `MDF`: Modify a kvpair's `value`.
- `RNM`: Rename a kvpair's `key`.
- `CPY`: Copy kvpair.
- `GET`: Get `value` by `key`.
- `DUMP`: Dump all kvpair in an array.
- `SHUT`: Close current TCP connection.

In `kvdb.h`:

```c
#define OPCODE_ADD "ADD"
#define OPCODE_DELETE "DEL"
#define OPCODE_MODIFY "MDF"
#define OPCODE_RENAME "RNM"
#define OPCODE_COPY "CPY"
#define OPCODE_GET "GET"
#define OPCODE_DUMP "DUMP"
#define OPCODE_CLEAR "CLR"
#define OPCODE_SHUTDOWN "SHUT"
```

## 0x01 Protocol (TCP)

> In big endian

### Data Format

1. Integer data format

```
<data_type(16 bits)>|<integer(64 bits)>
```

2. Float data format

```
<data_type(16 bits)>|<float(64 bits)>
```

3. String data format (integer, float, string)

```
<data_type(16 bits)>|<str_len(32 bits)>|[char(8 bits)]*str_len
```

4. Array format

```
<data_type(16 bits)>|<counts(32 bits)>|[data]*counts
```

5. Empty data

```
<data_type>
```

In `kvdb.h`:

```c
#define DATA_TYPE_EMPTY 0x0
#define DATA_TYPE_INTEGER 0x1
#define DATA_TYPE_FLOAT 0x2
#define DATA_TYPE_STRING 0x3
#define DATA_TYPE_ARRAY 0x4
#define DATA_TYPE_TERM 0xff
```

### Clitnt Message Format

```
"KVDB"|<op len(16 bits)>|<opcode>|[data]*n
```

> N indicates the number of parameters. Please refer to `supported methods`.

### Server Message Format

```
"KVDB"|data
```

> The reason for the `query failure` will be returned in `string` data format

### Supported methods

1. ADD(KEY,VALUE)
2. DEL(KEY)
3. MDF(KEY)
4. RNM(OLD_KEY, NEW_KEY)
5. CPY(SRC_KEY, DST, KEY)
6. GET(KEY)
7. DUMP()
8. CLR()
9. SHUT()

## 0x02 Build

1. `git clone https://github.com/yikesoftware/kvdb`

2. `cd kvdb`

3. make
   - Release: `make`
   - Debug: `make debug`
     - This will show `data_t` construction info and `handler return` in `stderr`.
   - Disable optimization: `make noopt`




