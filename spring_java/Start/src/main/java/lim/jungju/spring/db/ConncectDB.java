package lim.jungju.spring.db;

import java.sql.Connection;
import java.sql.SQLException;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;


@Repository
public class ConncectDB {
	
	@Autowired
	DataSource dataSource;
	public void conn() {
		Connection connection = null;
		try {
			connection = (Connection) dataSource.getConnection();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println(connection);
		
	}
}
