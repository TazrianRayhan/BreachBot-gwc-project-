#Breach Bot Part 3 Code
breachYear = 2017

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the National Health Services data breach in 2017")

#Introduces breach
print("Would you like to learn about the National Health Services data breach in 2017?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection.")
  topic = input()

  if topic.lower() == "a":
    print("The primary culprit was the WannaCry ransomware, a malicious software that infected computer systems worldwide.Patient records, appointment details, and other sensitive healthcare information were compromised.")
    print("WannaCry exploited vulnerabilities in outdated Windows operating systems, spreading through network connections. The ransomware encrypted files, demanding payment for their release. Hospitals and healthcare facilities were affected due to inadequate system updates and cybersecurity measures.")

  elif topic.lower() == "b":
    print("The NHS took immediate steps to contain the breach, isolating affected systems and applying patches to vulnerable software. Emergency response teams worked to restore data and enhance cybersecurity measures. The incident prompted a broader assessment of the NHS's cybersecurity practices, leading to increased investments in security technologies and staff training")

  elif topic.lower() == "c":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad (b) my reaction, (c) my advice, or (d) none.")
  topic = input()

  if topic.lower() == "a":
    print("The data breach directly compromised the confidentiality of patient records and sensitive healthcare information. WannaCry ransomware encrypted files, making them inaccessible to authorized users, thereby violating the principle of keeping data confidential and protected from unauthorized access. This breach highlighted the critical importance of safeguarding sensitive information in the healthcare sector.")

  elif topic.lower() == "b":
    print("I agree with the organization's response to the NHS data breach. The swift actions taken by the NHS, including isolating affected systems, applying patches, and implementing measures to prevent future incidents, reflect a proactive approach to mitigating the impact of the breach. The emphasis on enhancing cybersecurity measures, increasing investments in security technologies, and providing recommendations to affected users aligns with best practices for responding to such incidents.")
    print("However, it is crucial for the organization to continuously reassess and improve its cybersecurity protocols to stay ahead of evolving threats. Regular updates, ongoing staff training, and collaboration with cybersecurity experts are essential components of a robust defense against potential breaches. Overall, the organization's response demonstrates a commitment to learning from the incident and reinforcing its cybersecurity posture, which is commendable in the face of complex and persistent cyber threats.")

  elif topic.lower() == "c":
    print("I would advise them to regularly check their financial accounts for any unusual or suspicious activity. If they notice anything out of the ordinary, they should report it immediately to their financial institution. Ensure that antivirus and anti-malware software is up-to-date to defend against potential threats. Regularly update all software and applications to patch vulnerabilities and strengthen overall security.")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")