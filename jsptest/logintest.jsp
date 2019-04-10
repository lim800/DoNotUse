<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>로그인 페이지</title>
<script type="text/javascript" src="../js/jquery-1.11.2.js"></script>
</head>
<body>
	<form action="../logintest" method="get" enctype="application/x-www-form-urlencoded">
		<fieldset>
			<label for="id">아이디: </label> 
			<input type="text" name="id" id="id" required>
			<br/> 
			<label for="passwd">비밀번호: </label> 
			<input type="text" name="passwd" id="passwd" required>
			<br/> 
			<input type="submit" value="로그인">
		</fieldset>
	</form>

<script type="text/javascript">
	$(document).ready(function() {
	var TestId = /^[A-Za-z0-9]{3,10}$/; //아이디 유효성 검사 3~16자 사이
	var TestPasswd = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,20}$/; //패스워드 유효성 검사 8~20자 사이
	$("form").submit(function(){
		if ( !TestId.test($.trim($("#id").val())) )
		{
			alert("아이디 오류: 영문 대소문자,숫자 인식 (3~10자 사이)");
			$("#id").focus();
			return false;
		}
		if ( !TestPasswd.test($.trim($("#passwd").val())) )
		{
			alert("패스워드 오류: 영문,숫자,특수문자 혼합문자 (8~20자리 사이)");
			$("#passwd").focus();
			return false;
		}	
	});
});
</script>

</body>
</html>