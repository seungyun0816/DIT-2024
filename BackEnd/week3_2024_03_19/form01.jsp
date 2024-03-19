<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Form tag 연습</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
	<div class="container">
		<h2>회원가입</h2>
		<form action="form02.jsp" method="POST">
		
			<div class="form-group">아이디 : <input type="text" name="id"><br></div>
			<div class="form-group">이름 : <input type="text" name="name"><br></div>
			<div class="form-group">비밀번호 : <input type="PASSWORD" name="pwd"><br></div>
			
			<button type="submit" class="btn btn-primary">확인</button>
			<button type="reset" class="btn btn-primary">취소</button>
		</form>
	</div>
</body>
</html>