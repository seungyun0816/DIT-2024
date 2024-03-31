package com.example.counter;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    public TextView num1;

    public int cnum = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        num1 = findViewById(R.id.textview1);

    }
    public void plus(View view){

        ++cnum;

        num1.setText("Counter:"+cnum);
    }

    public void minus(View view){

        --cnum;

        num1.setText(("Counter:"+cnum));

    }
}
