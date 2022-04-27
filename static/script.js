window.addEventListener('load', 
  function() { 

    $.ajax({
        url: "http://127.0.0.1:5000/item-list",
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
            
            // response = $.parseJSON(response);
            items = res.item_list
            
            console.log(items);
            
            var html = '<table>';
            // build table headings
            html += '<thead><tr>';
            html += '<th> Items Present </th>';
            html += '</tr></thead>';
            html += '<tbody>';

            $.each(items, function (i, item) {
                console.log({item})
                html += '<tr><td>' + item + '</td></tr>';
            });
            
            html += '</tbody>';
            html += '</table>';

            $('.ml-container').append(html);

        }
    });


}, false);