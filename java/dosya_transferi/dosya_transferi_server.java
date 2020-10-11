
import java.io.*;
import java.net.*;

public class server {

    public static void main(String[] args) throws IOException {
        ServerSocket sv = new ServerSocket(30001);
        Socket con = sv.accept();
        InputStream inStream = con.getInputStream();
        OutputStream outStream = con.getOutputStream();
        FileOutputStream fos = new FileOutputStream("c:/datas/ornek.zip");
        //okunan veri fos nesnesine yaziliyor
        int len = 1;
        byte data[] = null;
        while (len != 0) {
            data = inStream.readAllBytes();
            len = data.length;
            fos.write(data);
            fos.flush();
        }

        /*  inStream.transferTo(fos);
       sadece yukarıdaki metotu kullanarakta yine tum veri fos nesnesine yazilabilirdi
         */
        fos.close();
        inStream.close();
        outStream.close();
        con.close();
    }

}
