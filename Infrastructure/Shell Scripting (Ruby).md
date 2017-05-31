# Shell Scripting (Ruby)

```Dir.entries "/"``` - Displays files in root

```Dir["/*.txt"]``` - Regex find all files w/ .txt ending

```print File.read("/comics.txt")``` - Prints contents of file

```FileUtils.cp('/comics.txt, '/Home/comics.txt')``` - Makes copy and puts it into right parameters

```
File.open("/Home/comics.txt","a") do |f|
  f << "Cat and Girl: http://catandgirl.com/"
end
```

- Opens up file and adds text into it

```File.mtime("/Home/comics.txt")``` - Prints times file was edited
