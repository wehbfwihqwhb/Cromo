import streamlit as st
import Pyttsx3
import random
engine = Pyttsx3.init()
engine.setProperty("rate", 174)
col,col1 = st.columns(2)
col.header("Cromolearners")
col1.text("Your history subject Artificial intelligence. This AI will give you a guide on how to go about answering your history essays and also provide a guideline.")
st.text("My name is Dr Eye-Ris. I will be helping you out in explainig you, your history essays of which are necessary in order for you to be able to pass your 12th grade. Could you please supply me with your name on box below before we even proceed.")
d = st.camera_input(label="Please take a picture of yourself") 
cho = ["You look absolutely great. You may proceed.", "Thank you for taking a picture, I definitely appreciate it.","Wow! At least i now know what you look like. You may proceed."]
choi = random.choice(cho)
if d:
    st.text(choi)
else:
          st.warning("Take a picture of yourself, please.")  
b = st.text_input("What is your name?")
col2,col3 = st.columns(2)
col2.image("data:image/jpeg;base64,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")
col3.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyQLKP3M3woGIwwE42JVQNN262QH1PWyJfFg&usqp=CAU")
def pp():
         with open("History p1 Qp.pdf", "rb") as file:
                btn = st.download_button(label="Download p1 question paper", data=file,file_name="History p1 Qp.pdf", mime="pdf")
         with open("History p1 Memo.pdf", "rb") as file:
                btn = st.download_button(label="Download His p1 memo", data=file,file_name="History p1 Memo.pdf", mime="pdf")
         with open("History p2 Qp.pdf", "rb") as file:
                btn = st.download_button(label="Download His p2 question paper", data=file,file_name="History p2 Qp.pdf",mime="pdf")
         with open("History p2 Memo.pdf", "rb") as file:
                btn = st.download_button(label="Download His p2 Memo", data=file,file_name="History p2 Memo.pdf",mime="pdf")                     
           

x = st.sidebar.radio("Navigation", options=["Home","Road to democracy", "Vietnam war", "BPM", "BCM", "Past papers and memos", "General tips"])

def rtd():
        engine.say("Road to democracy. This essay is all about how there were certain factors which led to the democratic elections and resistance from apartheid regime. What you need to know is, the national party was loosing and support during the strikes that were taking place in South Africa. Resistance organisations were now about to be unbanned because of factors such as the release of Nelson Mandela, the falling of the economy in South Africa because of strikes, the disinvenstments from European countries from South Africa, how the USSR and the USA made peace from the arms race. All these factors led to De Clerk in 1990 proposing the release of Nelson Mandela and unbanning parties such as ANC and PAC from exile. This was now the going to be the beginning of the negotiations between ANC and the National Party," + " " + b + " So then here's what you are supposed to write next. This is now about the meetings that took place. The first meeting between the ANC delegation which was led by Nelson Mandela and the NP delegation which was led by De Klerk was in 1990, held in Groot Schuur. In this meeting, the agreements which were made were, NP would release political prisoners from prison, it was also agreed that, there would be no more violence, and that ANC would prevent MK from operating. This meeting was then a success," + " " + b + "The second meeting took place again in 1990. During this meeting, which was held in Pretoria, hence it was called the Pretoria minute, it was also agreed between the two delegations that, there would be peace, no more violence and that, more prisoners would be released from prisons by the National Party. Then on the following year, what happened is the fact that, more political parties were present in the meeting, it was not only the ANC and NP delegation. Parties such as IFP, PAC and many others were there. Well, at first, IFP and PAC were against the negotiations but then, eventually they both came on board with the negotiations. During this meeting, it was agreed that South Africa should be a democratic country, and the fact that, there was supposed to be equity and equal rights amongst everybody. This meeting was also a success. Then during the year 1992, there was a bit of a problem. De Klerk was actually accused of selling out whites. Fortunately, thanks to his referendum that was made, he managed to win and gain over the support of many whites in South Africa to support the negotiations. On the very same year, a massacre took place in in a place called Boipatong. What happened is, the IFP hostelers were accused of attacking the Boipatong township and killing dozens of people. This incident therefore led to ANC withdrawing from the negotiations. A second massacre took place again in Bisho. It was when Cyril Ramaphosa led a march to Bisho which was not a success because of how they got attacked by the Bisho or Ciskei troops. This therefore led to Ramaphosa realizing that, negotiations had to take place all over again. Then during the year 1993, since a lot of political parties were still part of the negotiations, negotiations took place between them and traditional such as Chief Mangosuthu Buthelezi. Chief Mangosuthu Buthelezi decided to come out of the negotiations as he believed that, ANC was being unfair against other parties. As a result he joined forces with the Progressive Federal Party, forming COSAGU. The on the very same year, Chris Hani was assasinated. He was killed in cold blood outside of his own house. This caused the whole country to be angry and want to resort to violence. Luckily Nelson Mandela managed to calm down everyone not to resort to violence because of thi.s incident. This was then a success as it is the one that led to the set up of the democratic elections which would take place on the following year, 1994," + " " + " " + b + "This is the idea around the road to democracy essay")
        engine.runAndWait()
def vw():
        engine.say("The vietnam war was quite an interesting one. It was a war between a small group of vietnamese soldiers and the great United States of America")


if x == "Road to democracy":
        rtd()
        st.text("Road to democracy. This essay is all about how there were certain factors which led to the democratic elections and resistance from apartheid regime. What you need to know is, the national party was loosing and support during the strikes that were taking place in South Africa. Resistance organisations were now about to be unbanned because of factors such as the release of Nelson Mandela, the falling of the economy in South Africa because of strikes, the disinvenstments from European countries from South Africa, how the USSR and the USA made peace from the arms race. All these factors led to De Clerk in 1990 proposing the release of Nelson Mandela and unbanning parties such as ANC and PAC from exile. This was now the going to be the beginning of the negotiations between ANC and the National Party," + " " + b + " So then here's what you are supposed to write next. This is now about the meetings that took place. The first meeting between the ANC delegation which was led by Nelson Mandela and the NP delegation which was led by De Klerk was in 1990, held in Groot Schuur. In this meeting, the agreements which were made were, NP would release political prisoners from prison, it was also agreed that, there would be no more violence, and that ANC would prevent MK from operating. This meeting was then a success," + " " + b + "The second meeting took place again in 1990. During this meeting, which was held in Pretoria, hence it was called the Pretoria minute, it was also agreed between the two delegations that, there would be peace, no more violence and that, more prisoners would be released from prisons by the National Party. Then on the following year, what happened is the fact that, more political parties were present in the meeting, it was not only the ANC and NP delegation. Parties such as IFP, PAC and many others were there. Well, at first, IFP and PAC were against the negotiations but then, eventually they both came on board with the negotiations. During this meeting, it was agreed that South Africa should be a democratic country, and the fact that, there was supposed to be equity and equal rights amongst everybody. This meeting was also a success. Then during the year 1992, there was a bit of a problem. De Klerk was actually accused of selling out whites. Fortunately, thanks to his referendum that was made, he managed to win and gain over the support of many whites in South Africa to support the negotiations. On the very same year, a massacre took place in in a place called Boipatong. What happened is, the IFP hostelers were accused of attacking the Boipatong township and killing dozens of people. This incident therefore led to ANC withdrawing from the negotiations. A second massacre took place again in Bisho. It was when Cyril Ramaphosa led a march to Bisho which was not a success because of how they got attacked by the Bisho or Ciskei troops. This therefore led to Ramaphosa realizing that, negotiations had to take place all over again. Then during the year 1993, since a lot of political parties were still part of the negotiations, negotiations took place between them and traditional such as Chief Mangosuthu Buthelezi. Chief Mangosuthu Buthelezi decided to come out of the negotiations as he believed that, ANC was being unfair against other parties. As a result he joined forces with the Progressive Federal Party, forming COSAGU. The on the very same year, Chris Hani was assasinated. He was killed in cold blood outside of his own house. This caused the whole country to be angry and want to resort to violence. Luckily Nelson Mandela managed to calm down everyone not to resort to violence because of thi.s incident. This was then a success as it is the one that led to the set up of the democratic elections which would take place on the following year, 1994," + " " + " " + b + "This is the idea around the road to democracy essay")
elif x == "Past papers and memos":
       pp()
elif x == "Vietnam war":
       engine.say("Now,When it comes to the vietnam war against the USA, you have to keep in mind only one thing, that, there firstly was  a conflict in which the northern past of Vietnam and the southern part of vietnam were supposed to be combined together. Why was this the case? It is simply because the southern part of vienam was living in poor conditions, the king of the southern part of vietnam was also not treating the people in the southern part of vietnam in a good way as he would kill anybody who went against him. So, there was a meeting then between the UDF who were from the northern part of vietnam and the king of the south, Ngo Dihn Diem. This meeting was held because the COF wanted to ease the situation by asking Ngo Dihn Diem to allow the northern part of Vietnam and the Southern part of vietnam. However, Ngo Dihn Diem refused to make that happen. As a result the meeting was a failure. Then the UDF decide to take matters into its own hands by training soldiers who were commonly known as the Vietcong soldiers. The vietcong soldiers were sent to take down Ngo Dihn Diem and as a result, they managed to take him down. Now the southern part of Vietnam was under the control of these vietcong soldiers. So, what did the vietcong soldiers do then? They decided to create an underground tunnel callled the HO CHI MIHN TRILL. This tunnel was specifically created to help import goods and resources and food from the North to the south so that the people from the South would live much better. As a result, the leadership of the Vietcong soldiers, the people from the Southern part of Vietnam were living happily. What actually made the vietcong soldiers to be so effective, it was simply because they received full support from the USSR and China. They would receive anything from weapons, resources and many more from them, in order for them to be able to fight against USA which was highly against this arrangement of Vietnam as they feared that, communism would spread out the whole world. Then the USA decided to take action against this arrangement. The president of USA who was called, president Johnson decided to make an attempt to destroy the underground tunnel the Vietcong soldiers had been using to transport or import resources from the North. So he decided to throw bombs in the forest where he believed was located the HO CHI MIHN TRILL. Unfortunately this attempt was a failure as the bombs instead  damaged the wrong spots and damaged a lot of houses. Therfore this was a huge disgrace coming the USA." + b + "You have to understand that the USA made a lot of poor attempts which failed throughout this whole war. So what did president Johnson decide to do? He decided to use some chemicals to try and destroy the vietcong soldiers in the forests, which was also such an unfortunate thing to do because, these chemicals instead harmed and killed a lot of innocent people instead of the Vietcong soldiers. Therfore consequently, a lot of countries from around the world were so dissapointed from USA. This then as a result, led to the stepping down of president Johnson as president. Finaly on the year 1975, on the 30th of January, the Vietcong soldiers decided to finalise the whole war. On this day, it was when the Vietcong soldiers were holding a lot of funerals. They used the coffins and caskets to hide a lot of weapons which they used to succesfully attack all the air bases in the USA. This as a result, caused the United States to give up and be defeated. The war between the Vietcong and the USA lastly led to the official combination of the northern part of vietnam and the southern part of vietnam. This also led to the implementation of communism in the southern part of vietnam.")
       engine.runAndWait()    
elif x == "BPM":
       engine.say("OK! So, when it comes to the black power movement,You need to think of similar consequences and conditions as those that took place during apartheir in South Africa but, these conditions took place in America. OK! " + b + "So what actually happened in America was the fact that the black Americans were faced with dier and uncomfortable conditions as black people or the negroes. The reason why they were under such negative conditions happens to be the fact that, there was violence which was imposed upon the blacks by the poslice, by the KKK and so on. Black americans were killed each and evryday by the police force and the KKK. There were also laws which were imposed against the blacks by the police which were aimed at oppressing the balcks. The blacks were also receiving low wages compared to the whites. They were also denied job opportunities because of how inferior they were considered to be. Now, some people , blacks americans decided that, they need to stand up against such conditions and help ease the conditions and violence, along with the oppressions that were faced by the black Americans. So, that's when the black power movement was formed, was established. Well at first a leader who went by the name Martin Luther King emphasized that, peace can only be acquired without the use of violence. Howver, his approach was quite slow and was yielding poor results. So, what happened there on? A group of individuals such as Bobby and Newton simply formed a party of which they called, the black panther party. This party was going to fight agaist such conditions which were faced by the black americans. The balck panther party decided to form patrol groups, which would carrry guns and  weapons in order to protect the black Americans. As a result of this, the blacks were now feeling much more safe from the KKK and the violence imposed by the police. The KKK would get involved in shootouts with the police accross a lot of cities in America ,  as part of their mission. Now, lets talk a bit more about some of the members who were considered highly influential in all this movement. There was  a guy who went by the name Malcolm X. He instead came up with a different approach, an approach which would involve violence. Hence why he promoted the violence and retaliation methods which the black panther party was using, which was ,violence. His approach of violence was quite effective as change and progress was not slow against the oppresions faced by the black Americans. This movement was at this point considered as a greate threat against the whites to such a point that, Newton, one of the individuals who were behind the black panther party, was arrested for shooting and killing a police official. Now, party, had a ten point programme. In this programme they demanded equal job opportunities for the balck Americans, they had demande the KKK to stop violating the black americans, they also demanded the release of Black americans who were arrested for fighting for their rights, such as Rosa Parks. This programme was a very much greate success. The balck panther party also created other programmes which would help empower the societies of black Americans. These were were the healthcare facilities for black Americans, they also included the food programmes which would help provide breakfast for the balcks. They also included skills development programmes such as literacy skills to the black Americans. As a result of such programmes, the conditions faced by the black americans were now starting to improve because of the black panther party. Lastly, another influential individual was Stockey Carmichiel. He promoted that  blacks take pride in themselves, their heritage and their unique identity.")
       engine.runAndWait()
elif x == "BCM":       
       engine.say("For you to understand the black consciousness movement, you have to remember how it all started after the coming of PW Botha into power who introduced his total strategy. At this time, in the country, races such as indians, coloreds and blacks were not granted any rights outside their homelands. This was all to ensure that, the whites still remained at the top and superior compared to all the other races. At this time around these races were using violence to respond to such bad conditions which were imposed upon them by the  white goverment. As a result of this violence, the white goverment ensured that it bans ANC and PAC which were underground organizations. Leaders of such organizations were also sent into exile. The white goverment proceeded by introducing the terrorism act, which ensured that, it keeps the whites more powerful than all the other races. Then the goverment also ensured that it introduced the bantu education, which was to ensure that blacks received insufficient education, or poor education compared to whites. Basically, the apartheid goverment was in full control, suppressing the other races. This is the background information that will help you get a clear sense of how the BCM was formed. So here's the most important part. Well within the universities which were founded by the bantu education, there were a group of students who decided to show resistance against the apartheid goverment. Such students were the likes of Steve Biko. They were all part of a group they called NUSAS. Now, the problem with NUSAS is the fact that, it also involved white students. Steve Biko then was convinced that the whites would not really understand the issues faced by the blacks, coloreds and indians. So as a result, he decided to withdraw from NUSAS and formed his own organisation called SASO. SASO was only consisting of black students from around the universities such as University of Zululand. SASO then got to form its own philosophy. They believed the blacks and other races were supposed to be restored their identity. Steve Biko made all the other members to believe that, blacks and coloreds and Indians had to be free psychology. Biko believd that, blacks were supposed to take pride in themselves and their skin color and ways of thinking. He believd that blacks were supposed to fight for self liberation. So, Im sure you are wondering how did the apartheid goverment respond to this movement. Well the govement thought that, the black consciousness movement was a philosophy which would have no direct political impact. Now after that, it was really obvious that the black consciousness movemt was gaining a lot of power and recognition. Speeches were being made around the country by the members such as Steve Biko that, people should stand up and fight against the apartheid regime. The goverment was now aware that the movement was really posing as a threat. As a result of this intensity, a lot of people from around the country were now in support of the movement. We also have to keep in mind that, Steve Biko and many of his fello SASO members were expelled from universities as they were the ones who were behind all this. There was also another organisation which was formed called the South African Students Movement. It was instead full of school children especially from Soweto during the 1970s. These school children during 1976 deicded to form a march and protests down the streets of Soweto fighting against oppressions they faced in schools such as having to learn all their languages in Affrikkans. During their march on the 16th of June 1976, they were faced with a devastating incident as they were shot at by the police. As a result of this massacre, the blacks around the country resorted to protests nation wide. These protests included everything from boycotts and the damaging of the goverment's proprty such as offices and buildings. People were highly furious because of the incident that happened on the day of the 16th of June 1976. We should also keep in mind that, a lot students decided to join ANC and PAC in exile which also were on their own mission of fighting against the apartheid goverment. They received military training which helped them to be prepared for the missions which were executed by ANC and PAC in order to sabotage the goverment.")
       engine.runAndWait()
elif x == "General tips":
       engine.say("You must always remember to answer what the question is asking of you. If the question asks you to take a stance, whether you agree or disagree, you are supposed to answer that immediately in your introduction. And," + b + "You are supposed to make sure that, at the end of each paragraphy within your body, you include a line of argument, which is a general point of what the paragraph is all about.")
       engine.runAndWait()
