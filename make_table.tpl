%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>Информация о курсе:</p>
<table border="1">
  <tr>
  %for col in result:
    <td>{{col[1]}}</td>
    <td>{{col[2]}}</td>
    <td>{{col[3]}}</td>
  %end
  </tr>
</table>