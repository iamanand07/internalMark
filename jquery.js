$(document).ready(function()
{

  $("#singlejs").click(function()
  {
  		var s=0;
  		var cs=0;
  		var credit=[];
  		var gradeValue=[];
  		var i=0;
  		var j=0;
	    $("select").each(function()
	    {
		     var a=($(this).attr("credit"));
		     console.log("credit "+a);
		     credit[i]=parseInt(a);
		     i++;
	    });
	    $("select option:selected").each(function()
		{
		    var b=($(this).val());
		    console.log("value "+b);
		    gradeValue[j]=parseInt(b);
		    j++	
	    });
	    console.log(credit);
	    console.log(gradeValue);
	    for(i=0;i<j;i++)
	    {
	    	s=s+(credit[i]*gradeValue[i]);
	    	if(gradeValue[i]!=0)
	    	{
	    		cs=cs+credit[i];
	    	}
	    }
	    document.getElementById("ans").innerHTML=s/cs;
	    perc();
  });

});