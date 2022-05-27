---
title: "Poly Internship: Twenty One"
layout: post-sequential
permalink: /blogs/poly-internship/:year/:month/:day
categories: poly-internship
tags: rpa death bob mess messing password change plesk pcp cp2 cp8 guidelines acme monaco backup report
---
# Twenty-first day of internship

<span class="timestamp">[09:40]</span> I'm not even done with the daily quests yet but i alraedy got a task from Mr. <span class="disable-selection" ondblclick="this.innerHTML='Alan Kuik'">Supervisor</span>, so instead of forgetting about it, i gotta record it down of [course](#what-i-did-today).

<span class="timestamp">[10:09]</span> So, uh, word of advice, <span style="font-size:130%">before running any RPA, open the required apps or files first,</span> becaauusse, after typing out my first task here, i found that the RPA did not detect new emails, which meant it marked all the NAS as missing! Don't do that shit, don't mess up the track, which could lead to messing up the RPA.

I'm quite glad that at least, at the very hardcore least, that the UiPath RPA was robust enough to be able to fix up the mistake that occured this morning.

<span class="timestamp">[17:39]</span> gosh, i've been tired all day, and my back is demanding for a pressing massage. The hours flew so fast, faster than my grades. I didn't even do my apk bs today. so much thought, yet feels like nothingness. perhaps today is like the first chapter of ecclesiastes. 

### What i did today
* Change password for <span class="disable-selection" ondblclick="this.innerHTML='chefheman@hilliergroup.com.sg'">&lt;<b>REDACTED</b>: client email&gt;</span>
    * Updated via <span class="disable-selection" ondblclick="this.innerHTML='https://cp8.infospace.com.sg:8443/'">&lt;<b>REDACTED</b>: company email gui link&gt;</span>
    * Updated IT Information files in <span class="disable-selection" ondblclick="this.innerHTML='Infospace'">&lt;<b>REDACTED</b>: itp organization&gt;</span> Storage
* A Monthly <span class="disable-selection" ondblclick="this.innerHTML='ACME Monaco'">&lt;<b>REDACTED</b>: client name&gt;</span> Offsite Backup Check.
    * **NOTE FOR INTERN**: Keep note of the Internship Guidelines, there may be several copies of the files. I could only do this task because I searched for the previous intern's actual latest edited guidelines. I think I will put that as my pass down instead of the one that I was given. The following is how the the basic sequence is:
    1. Make a new email.
        * From: <span class="disable-selection" ondblclick="this.innerHTML='ia@infospace.com.sg'">&lt;<b>REDACTED</b>: company intern email&gt;</span>
        * To: <span class="disable-selection" ondblclick="this.innerHTML='alan@infospace.com.sg'">&lt;<b>REDACTED</b>: company supervisor email&gt;</span>
            * The 'To' field is set to the supervisor because you need to get their approval first, after that you can switch it out with <span class="disable-selection" ondblclick="this.innerHTML='shirley.lee@acmemonaco.com'">&lt;<b>REDACTED</b>: a client email&gt;</span>
        * Subject: "Data Offsite Backup check as of [DD MMM YYYY]"
    1. Obtain screenshots of both local & offsite backup via NAS
        1. Open file explorer, go to <span class="disable-selection" ondblclick="this.innerHTML='C:\\Users\\User\\Dropbox\\InfoSpace Common\\clients\\ACME Monaco'">&lt;<b>REDACTED</b>: reference file location&gt;</span>, and then open the <span class="disable-selection" ondblclick="this.innerHTML='ACME Monaco IT info.xlsx'">&lt;<b>REDACTED</b>: reference file name&gt;</span>
        1. Go to the “Server and Network Info.” tab, and under the “NAS'' section, you will see the login information for the NAS <span class="disable-selection" ondblclick="this.innerHTML='AMANAS'">&lt;<b>REDACTED</b>: client NAS&gt;</span>, as well as NAS <span class="disable-selection" ondblclick="this.innerHTML='AMANAOFFSITE'">&lt;<b>REDACTED</b>: client NAS&gt;</span>
        1. For now, click on the synology quickconnect link for <span class="disable-selection" ondblclick="this.innerHTML='AMANAS'">&lt;<b>REDACTED</b>: client NAS&gt;</span>, which is <span class="disable-selection" ondblclick="this.innerHTML='https://quickconnect.to/acmemonaco'">&lt;<b>REDACTED</b>: client quickconnect url&gt;</span>, then login with the credentials that you see, as of writing this the are"
            1. Username: <span class="disable-selection" ondblclick="this.innerHTML='infospace'">&lt;<b>REDACTED</b>&gt;</span>
            1. Password: <span class="disable-selection" ondblclick="this.innerHTML=';J@Q&V'">&lt;<b>REDACTED</b>&gt;</span>
        1. Once logged in, navigate to the "Main Menu", the icon in the top left, and then click on "Hyper Backup", as shown in the guide.
        1. Once in, screenshot the first one. 
    1. After you have pasted the screenshot in the email, you will need to do the steps for the following image.
        1. Using the information found in step 3c, go to <span class="disable-selection" ondblclick="this.innerHTML='https://quickconnect.to/acmemonacooffsite'">&lt;<b>REDACTED</b>: other client NAS&gt;</span>, and as of writing this, the credentials are the same as the one above.
        1. After getting in, head to "File Station" which is located on the desktop, and then right click on the <span class="disable-selection" ondblclick="this.innerHTML='AMANAS_1.hbk'">&lt;<b>REDACTED</b>: client NAS file&gt;</span>, and click "Open Backup Explorer".
        1. As stated in the guide, you should include the timeline at the bottom of the window when taking the screenshot
        1. Paste it to the email, send to supervisor for approval before sending it to <span class="disable-selection" ondblclick="this.innerHTML='Shirley'">&lt;<b>REDACTED</b>&gt;</span>
            * You can refer to emails made in the past by me.
    

{% include comments.html url=page.url %}

<input id="password-input" type="password" class="text-secret" onkeyup="unlock()" autocomplete="off">

<span class="disable-selection" id="truth" style="display:none;">Damn, a lot happened during the weekend, that I really should have like a live blog for my own life instead. i may add more details in the future<!--br><br>Now on a lighter note, there's this girl, all the way back from secondary school, and out of nowhere she decided to communicate with me. So, and <span class="disable-selection" ondblclick="this.innerHTML='Roy'">my accountable friend</span> knows this well (because damn we got similar problems to a tea), this girl has some red flags that I won't get too much into.--> </span>
