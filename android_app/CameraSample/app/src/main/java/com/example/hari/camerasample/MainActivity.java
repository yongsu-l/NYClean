package com.example.hari.camerasample;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import com.ibm.watson.developer_cloud.visual_recognition.v3.VisualRecognition;
import com.ibm.watson.developer_cloud.visual_recognition.v3.model.ClassifiedImages;
import com.ibm.watson.developer_cloud.visual_recognition.v3.model.ClassifyOptions;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.io.File;


public class MainActivity extends AppCompatActivity {

    Uri imageUri;
    ImageView result;
    String imgLocation;
    static final int REQUEST_IMAGE_CAPTURE = 1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button click = (Button)findViewById(R.id.camera);
        result = (ImageView)findViewById(R.id.imageView);
    }

    public void dispatchTakePictureIntent(View view) {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        imageUri = Uri.fromFile(new File(Environment.getExternalStorageDirectory(),"NYClean" + ".jpg"));
                //String.valueOf(System.currentTimeMillis()) + ".jpg"));
        Log.d("STATE",imageUri.getPath());
        imgLocation = imageUri.getPath();
        takePictureIntent.putExtra(android.provider.MediaStore.EXTRA_OUTPUT, imageUri);
        startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
        /*
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
        */

        ;
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
           // Bundle extras = data.getExtras();
            //Bitmap imageBitmap = (Bitmap)extras.get("data");
            //result.setImageBitmap(imageBitmap);

            // Creates Byte Array from picture
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            //imageBitmap.compress(Bitmap.CompressFormat.PNG, 100, baos); // Not sure whether this should be jpeg or png, try both and see which works best

            //Bitmap bitmap = imageBitmap;



//encodes picture with Base64 and inserts api key
            try {
                String info = URLEncoder.encode("image", "UTF-8") + "=" + URLEncoder.encode(Base64.encode(baos.toByteArray(), Base64.DEFAULT).toString(), "UTF-8");
                //info += "&" + URLEncoder.encode("key", "UTF-8") + "=" + URLEncoder.encode("APIKEY", "UTF-8");
                Log.d("STATE",info);

                new MysyncTask().execute(imgLocation);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

    class MysyncTask extends AsyncTask<String, String, String> {
         protected  String doInBackground(String ... params){
             try {
                 int count = params.length;
                 for (int i = 0; i < count; i++) {

                     VisualRecognition service = new VisualRecognition(VisualRecognition.VERSION_DATE_2016_05_20,"36ead01e60f21adb8f427d311c023d5e55abced7");

                     if (ContextCompat.checkSelfPermission(thisActivity,
                             Manifest.permission.READ_CONTACTS)
                             != PackageManager.PERMISSION_GRANTED) {

                         // Should we show an explanation?
                         if (ActivityCompat.shouldShowRequestPermissionRationale(thisActivity,
                                 Manifest.permission.READ_CONTACTS)) {

                             // Show an explanation to the user asynchronously -- don't block
                             // this thread waiting for the user's response! After the user
                             // sees the explanation, try again to request the permission.

                         } else {

                             // No explanation needed, we can request the permission.

                             ActivityCompat.requestPermissions(thisActivity,
                                     new String[]{Manifest.permission.READ_CONTACTS},
                                     MY_PERMISSIONS_REQUEST_READ_CONTACTS);

                             // MY_PERMISSIONS_REQUEST_READ_CONTACTS is an
                             // app-defined int constant. The callback method gets the
                             // result of the request.
                         }
                     }
                     File picture = new File("/storage/emulated/0/","NYClean.jpg");
                     FileInputStream imagesStream = new FileInputStream(picture);
                     ClassifyOptions classifyOptions = new ClassifyOptions.Builder()
                             .imagesFile(imagesStream)
                             .imagesFilename("NYClean.jpg")
                             .parameters("{\"classifier_ids\": [\"TrashIdentifier_1455385164\","
                                     + "\"SatelliteModel_6242312846\"],"
                                     + "\"owners\": [\"IBM\", \"me\"]}")
                             .build();
                     ClassifiedImages result = service.classify(classifyOptions).execute();
                     Log.d("RESULT",result.toString());

    /*
                     System.out.println(params[i]);
                     URL url = new URL("https://api.imgur.com/3/upload.xml");

                     URLConnection conn = url.openConnection();
                     conn.setDoOutput(true);
                     OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
                     wr.write(params[i]);
                     wr.flush();
*/
/*

                     File file = new File(textFileName);
                     HttpPost post = new HttpPost("http://echo.200please.com");
                     FileBody fileBody = new FileBody(file, ContentType.DEFAULT_BINARY);
                     StringBody stringBody1 = new StringBody("Message 1", ContentType.MULTIPART_FORM_DATA);
                     StringBody stringBody2 = new StringBody("Message 2", ContentType.MULTIPART_FORM_DATA);
//
                     MultipartEntityBuilder builder = MultipartEntityBuilder.create();
                     builder.setMode(HttpMultipartMode.BROWSER_COMPATIBLE);
                     builder.addPart("upfile", fileBody);
                     builder.addPart("text1", stringBody1);
                     builder.addPart("text2", stringBody2);
                     HttpEntity entity = builder.build();
//
                     post.setEntity(entity);
                     HttpResponse response = client.execute(post);
*/
                     if (isCancelled()) break;
                 }
             }catch (IOException e) {
                     throw new RuntimeException(e);
                 }
            return null;
        }
    }
}
