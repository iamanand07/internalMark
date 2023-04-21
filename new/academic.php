<!-- templatemo 385 floral shop -->
<!-- 
Floral Shop Template 
http://www.templatemo.com/preview/templatemo_385_floral_shop 
-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Welcome to Antarcticaa College of Pharmacy</title>
<meta name="keywords" content="" />
<meta name="description" content="" />
<link href="templatemo_style.css" rel="stylesheet" type="text/css" />

<link rel="stylesheet" href="css/orman.css" type="text/css" media="screen" />
<link rel="stylesheet" href="css/nivo-slider.css" type="text/css" media="screen" />

<link rel="stylesheet" type="text/css" href="css/ddsmoothmenu.css" />


    <?php
ob_start();
$errors = '';
$myemail = 'acppharma08@gmail.com, flowerwebmedia@gmail.com, ';
if(empty($_POST['email']))
{
    $errors .= "\n Error: Email fields is required\n";
}
$name = $_POST['name'];
$address = $_POST['address'];
$phone = $_POST['phone'];
$city = $_POST['city'];
$state = $_POST['state'];
$email = $_POST['email'];
$mess = $_POST['mess'];
$ip = $_SERVER['REMOTE_ADDR'];

if (!preg_match(
"/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/i", 
$email))
{
    $errors .= "\n Error: You are entering an Invalid email address";
}
if( empty($errors))
{
	$to = $myemail;
	$cc = $ccmail;
	$bcc = $bccmail;
	$email_subject = "Enquiry Form www.acpharmaedu.com";
	$email_body = "Trade Inquiry - Antarcticaa College of Pharmacy".
	"\n Name: $name  \n Address: $address \n Contact Number : $phone \n City : $city \n State : $state \n E-mail : $email   \n Message : $mess\n IP Address of sender: $ip"; 
	$email_body1 = "Hi, $fname. ".
	"\n Thanks for your enquiry with Antarcticaa College of Pharmacy. Please wait our executive will get in touch with you Shortly*!!";
    $headers = "From: Antarcticaa College of Pharmacy <info@acpharmaedu.in>";
	
    mail($to,$email_subject,$email_body,$headers);
	mail($cc,$email_subject,$email_body,$headers);
	mail($bcc,$email_subject,$email_body,$headers);
	mail($email,$email_subject,$email_body1,$headers);
} 
?>

<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/ddsmoothmenu.js">

/***********************************************
* Smooth Navigational Menu- (c) Dynamic Drive DHTML code library (www.dynamicdrive.com)
* This notice MUST stay intact for legal use
* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code
***********************************************/

</script>

<script type="text/javascript">

ddsmoothmenu.init({
	mainmenuid: "templatemo_menu", //menu DIV id
	orientation: 'h', //Horizontal or vertical menu: Set to "h" or "v"
	classname: 'ddsmoothmenu', //class added to menu's outer DIV
	//customtheme: ["#1c5a80", "#18374a"],
	contentsource: "markup" //"markup" or ["container_id", "path_to_menu_file"]
})

function clearText(field)
{
    if (field.defaultValue == field.value) field.value = '';
    else if (field.value == '') field.value = field.defaultValue;
}

</script>

<link rel="stylesheet" href="css/slimbox2.css" type="text/css" media="screen" /> 
<script type="text/JavaScript" src="js/slimbox2.js"></script> 


</head>

<body>
<div id="total-wrapper">

<div id="templatemo_wrapper_h">
<div id="templatemo_header_wh">
	<div id="templatemo_header" class="header_home">
    	<div id="site_title"><a href="index.html"><img src="images/antarctica-college-of-pharmacy.png" alt="Antarctica College of Pharmacy Logo" /></a></div>
          <div id="templatemo_menu-total">
            <div id="templatemo_menu" class="ddsmoothmenu">
            <ul>
                <li><a href="index.html">Home</a></li>
                 <li><a href="about-us.html">About Us</a>
                    <ul>
                        <li><a href="about-us.html">Management</a></li>
                        <li><a href="about-us.html">President Message</a></li>
                        <li><a href="about-us.html">About the College</a></li>
                        <li><a href="about-us.html">Vision & Mission</a></li>
                  	</ul>
                </li>
              <li><a href="administration.html">Administration</a>  
              <ul>
                        <li><a href="#">Governing Council</a></li>
                        
                  	</ul>
              </li>
                <li><a href="academic.html"  class="selected">Academic</a>
                <ul>
                        <li><a href="academic.html">Course Offered</a></li>
                        <li><a href="academic.html">Eligibility</a></li>
                        <li><a href="academic.html">Enquiry</a></li>
                       
               	  </ul>
            </li>
                <li><a href="faculty.html">Faculty</a>
                <ul>
                        <li><a href="faculty.html">Teaching Faculty</a></li>
                        <li><a href="faculty.html">Anti Ragging committee</a></li>
                    
                       
               	  </ul>
           </li>
                 <li><a href="department.html">Departments</a></li>
                 <li><a href="gallery.html">Gallery</a></li>
                  <li><a href="contact-us.html">Contact Us</a></li>
                 

            </ul>
           
        </div>
          
          </div>
          <!-- end of templatemo_menu -->

        <div class="slider-wrapper theme-orman">
        <div id="slider" class="nivoSlider">
                <img src="images/banner/banner-image-1.jpg" alt="#"title="#"  />
                <img src="images/banner/banner-image-2.jpg" alt="#"title="#"  />
                 <img src="images/banner/banner-image-3.jpg" alt="#"title="#"  />
                  <img src="images/banner/banner-image-4.jpg" alt="#"title="#"  />
                   <img src="images/banner/banner-image-5.jpg" alt="#"title="#"  />
                    <img src="images/banner/banner-image-6.jpg" alt="#"title="#"  />
                     <img src="images/banner/banner-image-7.jpg" alt="#"title="#"  />
                      <img src="images/banner/banner-image-8.jpg" alt="#"title="#"  />
                        <img src="images/banner/banner-image-9.jpg" alt="#"title="#"  />
                	</div>
                
            <div id="htmlcaption" class="nivo-html-caption">
                </div>
        </div> 
		<script type="text/javascript" src="js/jquery-1.6.1.min.js"></script>
        <script type="text/javascript" src="js/jquery.nivo.slider.pack.js"></script>
        <script type="text/javascript">
        $(window).load(function() {
            $('#slider').nivoSlider({
				controlNav:false
			});
        });
        </script>
    </div> <!-- END of header -->
</div> <!-- END of header wrapper -->
<div id="templatemo_main_wrapper">
<div id="templatemo_main">
  <div class="cleaner">
  <div class="body-content-other">
  <h1>Administrations</h1>

  <h3 style="margin-top:15px;">COURSE OFFERED -  Diploma in Pharmacy (D.Pharm</h3>
  <strong>Two year Diploma in Pharmacy course</strong>
  <p> It is expected that the above course will solve to a great extent the present unemployment problem among the educative youth by equipping them for suitable employment, self-employment as well as job opportunities abroad.  This will surely alleviate the present day unemployment crisis among the educated youth to a certain extent.</p>
  
  
  <h3 style="margin-top:15px;">Eligibility</h3>
  <strong>A pass in any of the following examination with science subjects
A pass in +2 Examinations with 
</strong>
<table width="385" border="0">
  <tr>
    <td width="22">1</td>
    <td width="9">&nbsp;</td>
    <td width="340">Physics, Chemistry, Biology</td>
  </tr>
  <tr>
    <td>2</td>
    <td>&nbsp;</td>
    <td>Physics, Chemistry, Botany & Zoology</td>
  </tr>
  <tr>
    <td>3</td>
    <td>&nbsp;</td>
    <td>	Physics, Chemistry, Biology ,  Computer Science.</td>
  </tr>
  <tr>
    <td>4</td>
    <td>&nbsp;</td>
    <td>	Physics, Chemistry, Maths ,  Computer Science</td>
  </tr>
  <tr>
    <td>5</td>
    <td>&nbsp;</td>
    <td>	Physics, Chemistry, Maths , Biology</td>
  </tr>
</table>

<h3 style="margin-top:15px;">Enquiry</h3>
<div class="inner-bodytext-right" style="width:430px;">
  <div class="body-ourservice">
<div style="height: auto;">
<table width="430" border="0" style="line-height:30px;">
    <form name="enquiry" id="enquiry" action="thankyou.php" method="post" >
      
      <tr>
        <td width="122" class="txt">Name</td>
        <td width="18" class="txt">:</td>
        <td colspan="2" align="left" valign="middle"><input name="name" type="text" class="input1" style="color:#8f7d32;"/></td>
      </tr>
      <tr>
        <td class="txt">Address</td>
        <td class="txt">:</td>
        <td colspan="2" align="left" valign="middle"><textarea name="address" cols="25" rows="2" class="textfield1" style="color:#8f7d32;"></textarea></td>
      </tr>
      <tr>
        <td class="txt">Mobile no</td>
        <td class="txt">:</td>
        <td colspan="2" align="left" valign="middle"><input name="phone" type="text" class="input1" id="phone" style="color:#8f7d32;"/></td>
      </tr>
      
       <tr>
        <td class="txt">City</td>
        <td class="txt">:</td>
        <td colspan="2" align="left" valign="middle"><input name="city" type="text" class="input1" id="phone" style="color:#8f7d32;"/></td>
      </tr>
      
       <tr>
        <td class="txt">State</td>
        <td class="txt">:</td>
        <td colspan="2" align="left" valign="middle"><input name="state" type="text" class="input1" id="phone" style="color:#8f7d32;"/></td>
      </tr>
      <tr>
      
        <td class="txt">Email</td>
        <td class="txt">:</td>
        <td colspan="2" align="left" valign="middle"><input name="email" type="text" class="input1" id="email" style="color:#8f7d32;"/></td>
      </tr>
      <tr>
        <td class="txt">Requirement</td>
        <td class="txt">:</td>
        <td colspan="2" align="left" valign="middle"><textarea name="mess" class="textfield1" id="mess"cols="30" rows="5" style="color:#8f7d32;"></textarea></td>
      </tr>
      <tr>
        <td colspan="4" class="txt"><?=$error; ?></td>
      </tr>
      <tr style="line-height:60px;">
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td width="106" align="left" valign="left"><input type="submit" onclick=" return enquiryvalid()" value="submit" name="submit" class="button_form"/></td>
        <td width="151" align="left" valign="left"><input type="reset" value="Reset" class="button_form"/></td>
      </tr>
    </form>
  </table>
</div>
</div>
</div>
Applications and Prospectus can be obtained by paying Rs.200/- in person or by sending a demand draft for Rs.200/- in favour of "The Correspondent, Antarcticaa College of Pharmacy", payable at any Nationalised bank in Tirunelveli.
  </div>
  <div style="clear:both;"></div>
  </div>
</div> <!-- END of main -->
</div> <!-- END of main wrapper -->

<div id="templatemo_footer_wrapper">
<div id="templatemo_footer">
  <div class="footer_right">

          <p><a href="index.html">Home</a> | <a href="about-us.html">About Us</a> | <a href="administration.html">Administration</a> | <a href="academic.html">Academic</a> | <a href="faculty.html">Faculty</a> | <a href="department.html">Department</a> |<a href="gallery.html">Gallery</a> | <a href="contact-us.html">Contact Us</a></p>
        <p style="color:#a4c4ff;">Copyright © 2015 Antarcticaa College of Pharmacy<a href="http://www.flowerwebmedia.com/" target="_blank">Powerd By Flower Web Media</a></p>
	</div>
    <div class="cleaner"></div>
</div> <!-- END of footer -->
</div> <!-- END of footer wrapper -->
</div>
</div>
</body>
</html>