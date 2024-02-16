**Position indicators**
^ - start
$ - end

**Characters or groupings**
. - any character
[] - range or options for characters (e.g. "[a-z]")
[^] - not in a range or set of characters (e.g. "[^0-9a-zA-Z]" as non alpha-numeric)
() - grouping, can allow multiple options with "|" (e.g. "(2041|9044)")
\ - escape character

**Match multiple**
\* - 0 or more
\+ - 1 or more
{n} -  n times




**Regex epressions**
- Detecting preprocessor commands (lines starting with "#"):
  - grep "^#.*" -E hello.c -o