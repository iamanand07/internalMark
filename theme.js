var a=0;
var c;
var b;
function perc()
{
	if(screen.width<750)
	{
		document.getElementById("perc-resp").style.backgroundColor="white";
	}
	clearInterval(b);
	a=0;
	c=document.getElementById("ans").innerHTML;
	b=setInterval(increse,25);
	function increse()
	{
		if(a>=Math.round((c)*10))
		{
			clearInterval(b);
		}
		else
		{
			a++;
			document.getElementById("percentage").style.width=(a)+"%";
			document.getElementById("percentage").innerHTML=(a)+"%";
		}
	}
}
var wid=0;
function disp()
{
	var tr=-100;
	if(wid==0)
	{
		cle=setInterval(view,1);
	}
	function view()
	{
		if(tr==0)
		{
			clearInterval(cle);
		}
		else
		{
			tr++;
			wid=wid+2;
			document.getElementById("nav").style.transform="translateX("+(tr)+"%)";
			if(screen.width>480)
			{
				document.getElementById("cont").style.marginLeft=wid+"px";
			}
		}
	}
}
function closeit()
{
	var tr=0;
	cle=setInterval(noview,1);
	function noview()
	{
		if(tr==-100)
		{
			clearInterval(cle);
		}
		else
		{
			tr--;
			wid=wid-2;
			document.getElementById("nav").style.transform="translateX("+(tr)+"%)";
			if(screen.width>480)
			{
				document.getElementById("cont").style.marginLeft=wid+"px";
			}
		}
	}
}
