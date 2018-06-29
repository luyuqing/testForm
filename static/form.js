<script>
    $("form").submit(function(){
        $("#result").text("successssss");
    });
</script>





/* <script>
$(document).ready(function(){
    $("form").submit(function(event){
        $.ajax({
            type : "POST",
            url : '/',
            data: $(this).serialize(),
            success: function (data) {
                $("#result").text(data.name);
            }
        });
        event.preventDefault();
    });
});
</script> */
/* <script>
    function loadXMLDoc()
    {
        var req = new XMLHttpRequest()
        req.onreadystatechange = function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    document.getElementById('result').innerHTML = "Error"
                }
                else
                {
                    var response = JSON.parse(req.responseText)
                    document.getElementById('result').innerHTML = response.name
                }
            }
        }
    
        req.open('POST', '/')
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        var un = document.getElementById('name').value
        var sec = document.getElementById('age').value
        var postVars = 'name='+un+'&age='+sec
        req.send(postVars)
        
        return false
    }
</script> */