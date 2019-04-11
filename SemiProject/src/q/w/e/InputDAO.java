package q.w.e;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class InputDAO
{
	
	public ArrayList<storageDTO> Input(int deptno , String dname , String loc) {
	
	ArrayList<storageDTO> arrayList = new ArrayList<storageDTO>(); 
	
	Connection connection = null;
	PreparedStatement preparedStatement = null;
	
	try {
		Context context = new InitialContext();
		DataSource dataSource = (DataSource) context.lookup("java:comp/env/jdbc/oracledb");
		connection = dataSource.getConnection();
		String sql = "insert into dept (deptno,dname,loc) ";
		sql += " values (?,?,?)";
		preparedStatement = connection.prepareStatement(sql);
		preparedStatement.setInt(1, deptno);
		preparedStatement.setString(2, dname);
		preparedStatement.setString(3, loc);
		preparedStatement.execute();
		
		
	} catch (Exception e) {
		e.printStackTrace();
	}
	return arrayList; 
	
	}
	
	
	

}
