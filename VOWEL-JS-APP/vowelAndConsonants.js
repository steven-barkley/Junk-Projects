function vowelsAndConsonants(s) 
{
    vowels = ['a','e','i','o','u'];
    result = "";
    result2 = "";
    for(vowel=0; vowel < s.length; vowel++)
    {   
        // if a,e,i,o or u contained in s print out "variable"
        if (s.includes(s[vowel])) 
        {
            if (vowels.includes(s[vowel]) )
            {
                result += s[vowel];
            }
            else
            {
                result2 += s[vowel];
            }

        }
    }   
    vowelCollection = "";
    consonantsCollection =""; 
    for(y=0; y<result.length; y++)
    {
        vowelCollection += (result[y]);
    }
    for(z=0; z<result2.length; z++)
    {
        consonantsCollection += (result2[z])
    }
    return "\nYour string contains these vowels: " + vowelCollection + " and these consonants " + consonantsCollection+"\n";
}

alphabet = "abcdefghijklmnopqrstuvwxyz";

console.log(vowelsAndConsonants(alphabet));