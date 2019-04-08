<%@page import="org.omg.CORBA.Request"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="a.b.c.testDTO" %>
<%@ page import="java.net.URLEncoder" %>

<% request.setCharacterEncoding("UTF-8"); %>
<%

String user = request.getParameter("user");

testDTO test = new testDTO();
test.setUser(user);
user = test.getUser();
request.setAttribute("user", user);
//user = URLEncoder.encode(user,"UTF-8");
//response.sendRedirect("./view.jsp?user=" + user);
pageContext.forward("./view.jsp");

%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>control</title>
</head>
<body>


</body>
</html>