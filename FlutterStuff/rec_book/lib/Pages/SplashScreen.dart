import 'package:flutter/material.dart';

class SplashScreen extends StatefulWidget{
    @override
    _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>{
    @override 
    void initState(){
        super.initState();
        _navigateToHome();
    }
    void _navigateToHome() async {
        await Future.delayed(Duration(seconds: 3));
        /* Navigator.pushReplacement(
            context,
            MaterialPageRoute(builder: (context => Camerascreen))
        ), */
    }
    @override
    Widget build(BuildContext context){
        return Scaffold(
            backgroundColor: Colors.black,
            body: Center(
                child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                        Text(
                            'RecBook',
                            style: TextStyle(
                                fontSize: 48,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                            ),
                        ),
                        SizedBox(height: 15),
                        Container(
                            width: 100,
                            child: LinearProgressIndicator(
                                minHeight: 3,
                                valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                            ),
                        ),
                    ],
                ),
            ),
        );
    }
}