
import java.io.*;
import java.net.*;

public class client {

    public static void main(String[] args) throws IOException {

        Socket soket = new Socket("localhost", 30001);//localhost'a 30001 nolu porta baglanti aciyoruz
        OutputStream outStream = soket.getOutputStream();
        InputStream inStream = soket.getInputStream();
        FileInputStream fis = new FileInputStream("c:/datas/test.zip");//Servere gönderilecek file path
        //veri streame yazılıyor
        int len = 1024 * 1024;
        byte data[] = null;

        while (fis.available() != 0) {
            data = fis.readNBytes(len);
            outStream.write(data);
            outStream.flush();
        }//

        /* fis.transferTo(outStream);
       sadece yukarıdaki metotu kullanarakta tum veri streame yazilabilirdi.
         */
        fis.close();
        inStream.close();
        outStream.close();
        soket.close();

    }

}
