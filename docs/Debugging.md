# The Python Debugger

## Interactive Use

* Loading and starting the debugger

  ```
  import pdb
  pdb.set_trace()
  ```

* PDB simple commands

  | key | Mnemonic  | Function
  |-----|-----------|--------------------------
  | l   | list      | Shows current line
  | n   | next      | Execute line, move to next
  | h   | help      | Provides documentation
  | arrows up, down | | Move up, down to command history

* PDB advanced commands

  | key | Mnemonic  | Function
  |-----|-----------|--------------------------
  | w   | where     | Show stack trace
  | c   | continue  | Continue normal program flow
  | b   | breakpoint| Set breakpoint
  | s   | step into | Step down into next level
  | r   | return    | Step out of this level

  * Setting breakpoint with `file:lineno`

    ```
    b hello.py:2
    ```

  * Setting breakpoint with `file.function_name`

    ```
    b hello.index
    ```

## Resources

* **Pdb official ducumentation**
  * https://docs.python.org/3/library/pdb.html
* Article about pdb
  * http://www.onlamp.com/pub/a/python/2005/09/01/debugger.html
