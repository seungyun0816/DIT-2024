package com.example.widgetexample1;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    EditText eText1;
    EditText eText2;
    EditText eText3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EdgeToEdge.enable(this);
        Button bPlus = (Button) findViewById(R.id.button1);
        Button bMinus = (Button) findViewById(R.id.button2);
        Button bMulti = (Button) findViewById(R.id.button3);
        Button bDivide = (Button) findViewById(R.id.button4);
        eText1 = (EditText) findViewById(R.id.edit1);
        eText2 = (EditText) findViewById(R.id.edit2);
        eText3 = (EditText) findViewById(R.id.edit3);
    }

    public void cal_plus(View e) {
        String s1 = eText1.getText().toString();
        String s2 = eText2.getText().toString();

        int result = Integer.parseInt(s1) + Integer.parseInt(s2);
        eText3.setText("" + result);
    }

    public void cal_minus(View e) {
        String s1 = eText1.getText().toString();
        String s2 = eText2.getText().toString();

        int result = Integer.parseInt(s1) - Integer.parseInt(s2);
        eText3.setText("" + result);
    }

    public void cal_multi(View e) {
        String s1 = eText1.getText().toString();
        String s2 = eText2.getText().toString();

        int result = Integer.parseInt(s1) * Integer.parseInt(s2);
        eText3.setText("" + result);
    }

    public void cal_divide(View e) {
        String s1 = eText1.getText().toString();
        String s2 = eText2.getText().toString();

        int result = Integer.parseInt(s1) /  Integer.parseInt(s2);
        eText3.setText("" + result);
    }
}
