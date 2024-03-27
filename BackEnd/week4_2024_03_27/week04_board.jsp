<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<form action="week04_boardpro.jsp" method="get">
	작성자 :	<input type="text" name="boardName"><br>
	제목 : 	<input type="text" name="boardTitle"><br>
	지역	: 		<select name="boardLocation">
					<option value="seoul">서울</option>
					<option value="busan">부산</option>
					<option value="daegu">대구</option>
					<option value="incheon">인천</option>
					<option value="gwangju">광주</option>
					<option value="daejeon">대전</option>
					<option value="ulsan">울산</option>
				</select><br>
	내용	:	<input type="text" name="boardContent"><br>
			<input type="submit" value="확인">
			<input type="reset" value="취소">
	</form>
</body>
</html>