#variable

$inputFile=$args[0]
$duration=$args[1]

#read function: read line by line inputFile

foreach($line in Get-Content "$inputFile") {
    if($line -notmatch '^#.*'){
        #Work here
        if($line -notmatch '^\s*$'){
            $Word=$line.Split(" ")
            foreach($eachWord in $Word){
                Write-Output "$eachWord`:$duration"
            }
        }
        else {
            Write-Output "pause:0.25"
        }
    }
}