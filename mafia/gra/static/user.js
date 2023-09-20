function user_add(obj)
{
    var gracze = document.getElementsByClassName("gracz");
    var result = []
    for ( var i=0;i<gracze.length;i++)
    {
        result.push(gracze[i].value)
    }
    //gracze.forEach(element => {
      //  console.log(element);
    //});
    console.log(result);
    console.log("Żyjesz?");
    $.ajax({
      url: 'gra/dodaj_graczy',
      type: "POST",
      dataType: "json",
      data: {'users' : result},
      success: (data) => {
        console.log(data);
      },
      error: (error) => {
        console.log(error);
      }
    });
}