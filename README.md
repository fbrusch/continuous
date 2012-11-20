# Continuous

Continuous is a wrapper that allows to invoke a command in *continuous mode*, i.e. to reinvoke it whenever a given files changes.
Just invoke the command, and wrap in :w

Usage:

    > echo "" >hello.txt
    > continuous cat _hello.txt_
    > echo "hello" >>hello.txt
    hello
    > echo "hello again" >>hello.txt
    hello
    hello again
