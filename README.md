# ArtFont
utils required when building a artistic glyph dataset,including fontglyph rendering,obtaining  attributes of a font file,fonts filter,etc.

| tool | description |
| --- | --- |
| fontglyph rendering  | (ttf,char) -> (fontglyph) |
| fonts filter  | (font set) -> (font subset) |
| font parser  | (font) -> (font attribute) |
| glyph visualization  | (glyph dir \| glyphs) -> (image) |
| meta data |(scale) -> (meta data) |
| artistic glyph  | (font glyph,texture image) -> (artistic glyph) |

## flow
1. get the supported chars
    1.  build a raw dataset 
    2.  sample and view the images,choose the faults
    3.  collect the faults
    4.  filter the faults in ttf files and get the supported chars
2. filter invalid fonts
    1.  build a raw dataset
    2.  sample and view the images,record the invalid fonts
    3.  filter the invalid fonts
3. generate meta data
    1. build a map of name to path of font or color 
    2. use the meta module to generate meta data
4. build a artistic glyph dataset
    1. build a dataset using the synthesis module according to the meta data

## usage

### fontglyph rendering

### fonts filter

### visualization

### generate meta data


### build artistic glyph dataset



## jargons
1. **font**: a font is a collection of glyphs, each of which represents a character.
2. **glyph**: a glyph is a vector representation of a character.
3. **typeface**: a typeface is a collection of glyphs, each of which represents a character.
4. **texture**: a texture is a 2D image that represents a character.
5. **gradient** : a gradient is a 2D image that represents a character.
6. **fontglyph** : a grayglyph is a 2D image that represents a character.
7. **ttf/otf** : two types of font files.ttf is a TrueType font file,otf is a OpenType font file.


## reference

https://zi-hi.com/

## requirements
| 依赖项 | 说明 |
| --- | --- |
| python | the programming language |
| numpy |  image processing|
| PIL | image load and processing |
| fontTools | font file parsing |
