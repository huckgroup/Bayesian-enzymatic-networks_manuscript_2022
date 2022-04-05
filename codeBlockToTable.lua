--[[ MIT License
Copyright (c) 2022 Will Robinson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
]]

function createTableElement(filename)
    -- Reads in the file given by the path filename
    -- and outputs a new pandoc table element
  
    local f = io.open(filename, "r")
  
    if f ~= nil then
      local csv = f:read("*all")
      f:close()
      local new_section = pandoc.read(csv, "csv")
      return new_section
    end
  
    return nil
  
  end
  
  function CodeBlock(e)
    -- turns a CodeBlock element into a table
    local caption = e.text
    local filename = e.attr.classes[1]
  
    if filename == nil then
      return e
    end
  
    if string.match(filename,"csv") then
      local new_section = createTableElement(filename)
  
      if new_section ~= nil then
        local ast_table = new_section.blocks[1]
  
        ast_table.caption.short = {pandoc.Str(caption)}
  
        return ast_table
      end
    else
      return e
    end
  end
  
  -- function Div(e)
  --   -- turns a Div element into a table
  --   local caption = e.content[1].content[1]
  
  --   local filename = e.attr.classes[1]
  
  --   if filename == nil then
  --     return e
  --   end
  
    
  --   if string.match(filename,"csv") then
  --     local f = io.open(filename, "r")
  --     local csv = f:read("*all")
  --     f:close()
  
  --     local new_section = pandoc.read(csv, "csv")
  
  --     local ast_table = new_section.blocks[1]
  
  --     ast_table.caption.short = {pandoc.Str(caption)}
  
  --     return ast_table
  --   else
  --     return e
  --   end
  -- end
  