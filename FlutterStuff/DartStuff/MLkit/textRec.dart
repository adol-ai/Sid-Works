import 'dart:io';
import 'package:google_ml_kit/google_ml_kit.dart';

Future<void> main() async{
    final textRec = GoogleMlKit.vision.textRecognizer();
    try{
        final img = InputImage.fromFilePath("assets/text2.jpg");
        final RecognisedText outTxt = await textRec.processImage(img);
        print(outTxt.text);
    } catch (e){
        print("Error Yooo! $e");
    } finally{
        textRec.close();
    }
}