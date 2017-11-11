package com.example.muy.camera;

import android.content.Intent;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.io.File;


public class MainActivity extends AppCompatActivity {

    private Button btn;
    static final int cam_request = 1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn =(Button) findViewById(R.id.button);
        btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                File f2=getFile();
                intent.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(f2));
                startActivityForResult(intent, cam_request);
            }
        });
    }
    public File getFile(){
        File f1 = new File("sdcard");
        if(!f1.exists()){
            f1.mkdir();
        }
        File img = new File(f1,"img.jpg");
        return img;
    }
}
