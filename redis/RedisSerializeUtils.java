package io.renren.config;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

import io.renren.common.exception.RRException;

public class RedisSerializeUtils {

	  /**
	   * 将对象-->byte[] (由于jedis中不支持直接存储object所以转换成byte[]存入)
	   *
	   * @param object
	   * @return
	   */
	  public static byte[] serialize(Object object) {
	    try (ByteArrayOutputStream baos = new ByteArrayOutputStream();
	        ObjectOutputStream oos = new ObjectOutputStream(baos);) {
	      // 序列化

	      oos.writeObject(object);
	      byte[] bytes = baos.toByteArray();
	      return bytes;
	    } catch (Exception e) {
	      throw new RRException("serialize error", e);
	    }
	  }

	  /**
	   * 将byte[] -->Object
	   *
	   * @param bytes
	   * @return
	   */
	  public static Object unserialize(byte[] bytes) {
	    try (ByteArrayInputStream bais = new ByteArrayInputStream(bytes);
	        ObjectInputStream ois = new ObjectInputStream(bais);) {
	      // 反序列化
	      return ois.readObject();
	    } catch (Exception e) {
	      throw new RRException("unserialize error", e);
	    }
	  }

}
