<?php 
if(isset($_POST['submit'])){

$name = $_POST['Name'];
$visitor_email = $_POST['Sender'];
$subject = $_POST['Subject'];
$message = $_POST['Message'];


// $name = "Raj";
// $visitor_email = "demo@gmail.com";
// $subject = "testing";
// $message = "mail testing";


$email_from = 'amanmourya000097@gmail.com';

$email_subject = 'New Form Submission';

$email_body = "User Name: " . $name.
                "\n User Email: " . $visitor_email.
                "\n Subject: " . $subject.
                "\n Message: " . $message."\n";

$to = "amanmourya0097@gmail.com";

$headers = "From: $email_from \r\n";

$headers .= "Reply-To: $visitor_email \r\n";

if(mail($to, $email_subject, $email_body, $headers)){
	echo "Email Sent";
} else {
	echo "Email failed";
}
header("Location: contact.html");

}
?>