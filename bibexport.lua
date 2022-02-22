local citation_ids = {}

function Doc(body, meta, vars)
  local citations = {};
  for cid, _ in pairs(citation_ids) do
    citations[#citations + 1] = cid
  end
  -- create a dummy .aux file
  local aux = '\\bibstyle{alpha}\n' ..
      '\\bibdata{' .. meta.bibliography .. '}\n' ..
      '\\citation{' .. table.concat(citations, ',') .. '}\n'
  local auxfile_name = meta.auxfile or 'bibliography.aux'
  local auxfile = io.open(auxfile_name, 'w')
  auxfile:write(aux)
  auxfile:close()
  os.execute('bibexport -o bibliography.bib bibliography.aux ')
  return 'Output written to bibliography.bib, aux to ' .. auxfile_name
end

function Cite(c, cs)
  for i = 1, #cs do citation_ids[cs[i].citationId] = true end
  return ''
end

function Str(s) return s end
setmetatable(_G, {__index = function() return function() return "" end end})    