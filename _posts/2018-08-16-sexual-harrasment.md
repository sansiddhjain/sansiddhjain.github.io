---
title:  "Viewing Sexual Harassment in India Through the Lens of Probability"
date:   2018-10-16 12:00:00
categories: text
---

India's having its own #MeToo movement! A lot of the cases deal with sexual harassment at the workplace, and the timing couldn't have been more apt - the past week, we celebrated the 1 year anniversary of the [New York Times](https://www.nytimes.com/2017/10/05/us/harvey-weinstein-harassment-allegations.html) and [New Yorker](https://www.newyorker.com/news/news-desk/from-aggressive-overtures-to-sexual-assault-harvey-weinsteins-accusers-tell-their-stories) articles on Harvey Weinstein that shook the world, and started the #MeToo movement.

A striking similarity one may notice across several of these cases, is that a third party, and in most scenarios, third party in the position of power to do something about the case, knew about the transgressions and yet chose to do nothing about them. Now when the victim speaks up to the world, usually well after the incident has happened, the third party is often left scrambling to improve its image, and in a haste severs ties with the accused, issues profuse apologies, etc etc. I was too intrigued by why so many people, despite being in the position of power to do something about incidents of sexual harassment, chose to do nothing about it, and in effect, gave such incidents tacit approval. I was wondering if some concepts from decision theory and probability can be used to model such situations, and hopefully, we may gain some insights into why we're witnessing these trends. Here goes an attempt at doing that!

## The Model

*Note - The inspiration for doing such modelling came from Decision Theory (and it forms the basis of Markov Decision Processes). The technically inquisitive reader can read more about them [here](https://en.wikipedia.org/wiki/Decision_theory) and [here](https://en.wikipedia.org/wiki/Markov_decision_process)*

*Also Note - In this particular case I have talked about predatory sexual behaviour to be where the perpetrator is male, and the victim is female. Predatory sexual behaviour is most certainly not be restricted to that.*

Hypothetical situation - Suppose you're Mr. Maytan, the boss-man of a comedy company. A female employee comes and tells you in detail about an incident where she was sexually assaulted by a fellow employee a while back. This employee is indeed important for your company - he brings in a good amount of revenue. You confront that alleged perpetrator, and the explicit denial turns into a hesitant acceptance upon persistent questioning. Now the ball's in your court - you have a decision to make. Suppose the world is really simplistic, with few decision making options - you can either fire him, or choose to continue working with him as your employee (no tertiary arrangements such as freelancing can be worked out in this world!). However, certain things are not under your control - your female employee may choose to speak up to world about this incident, and that will end up having significant consequences on the functioning of your company, depending upon what action you choose to take with the perpetrator. You choose to make the decision matrix, the rewards of whose entries you are totally unclear about, yet. 

|                |Fire Employee		|Don't Fire Employee	|
|----------------|-------------------------------|
|She speaks up to the world| `Unknown`|`Unknown`|
|She doesn't speak up      |`Unknown`|`Unknown`|

Now that this fancy matrix is made, you go on to create an even fancier representation of the situation, a decision graph, that clearly encapsulates what would happen when you, the agent, takes an action, and when the environment is in a particular configuration (ie, your female employee speaks up, or not). Based on your intuition on how things would pan out, you make the following graph - 

![Alt text](https://sansiddhjain.github.io/graph1.svg)

If you fire the employee, and she does speak up, the world gives you a pat on the back. They laud you for doing the right thing, and people trust your company more. If you do fire the employee, and your female employee does not speak up, you may not be in the best situation monetarily, but hey, your care about the culture of your company too, and your conscience is clear that you took a step forward in creating a safe environment for women at your firm. If you don't fire the employee, and she does speak up, that's a PR shitstorm, the absolute worst position for you to be in. If you don't fire the employee, and she does not speak up, monetarily things are the status quo, but if you're a man conscious about the social implications of your actions, would you be able to sleep soundly at night?

You decide to assign numerical "rewards" to each state. On what basis would you assign these rewards? Well obviously monetarily, because you're a _dhandha_ (business), - it's ruthless, dog-eat-dog world, and at the end of the day, the only question that matters is _deti kitna hai?_ (how much does it give/earn)?

Suppose you don't fire the employee, and she doesn't speak up, and things remain the status quo - your employee is as valuable to you as the revenue he generates for you; for the sake of this discussion, assume that that is 5L by the end of the next quarter. Say you don't fire him, and then she does speak up - that is a shitstorm. You have to fire the guy immediately, so the revenue he could have generated for you is gone. Plus people start this entire #BoycottMaytan campaign and stop watching your videos, your collaborators stop working with you (you may even end up losing your job), you have to hire this law firm specialising in crisis PR and they charge an exorbitant bill and all. In short, you end up losing roughly 10L, making it's reward equal to -10L (If you think the negative reward is too small in magnitude, please hang on).

Say you fire him, and she doesn't speak up. Well, you're without a key employee now, and you go out into the world trying to find a replacement, and that takes time, effort, and money. The replacement would also happen sufficiently into the future, and you care much more about immediate returns as compared to the future ones, so you award a 0.8 decay factor to the revenue the replacement would bring. If you fire the employee, and she does speak up, you get good PR, but that does not make you gain much monetarily. It's a free brownie courtesy the world, and that's it. It gets a token reward of 10000 INR (Those who disagree and think this reward is too low, please hang on). You still have to go out and try to find a new replacement like in the previous case, so the revenue brought in by the new guy is also added with the decay factor.

Now you think, what is the chance that your female employee would speak up? You are being very conservative here, because you are suddenly a very cautious man. You assume on an average, 4% of all women would speak up about sexual harassment at the workplace, even though you know that the figure is waaay higher than what is the reality. ([Read this](https://www.livemint.com/Politics/AV3sIKoEBAGZozALMX8THK/99-cases-of-sexual-assaults-go-unreported-govt-data-shows.html)). You then get this decision tree.

![Alt text](https://sansiddhjain.github.io/graph6.svg)

# Inference

Now let's back up the probabilities, and calculate the expected reward of taking each action. Time to bring in the math!

Let the following denote - 

\\(s\\) :  The event that the female employee speaks up

\\(\overline{s}\\) :  The event that she doesn't

\\(f\\) : Employee (the perp) is fired

\\(\overline{f}\\) : Employee (the perp) is not fired

\\(P(e)\\) :  Probability of event \\(e\\) happening

\\(R(e, a)\\) :  The Reward, if action \\(a\\) was taken, and event \\(e\\) happened

\\(E(a)\\) :  The Expected reward, of taking action \\(a\\)

The expected reward of firing the employee would be

$$ E(f) = P(s)*R(s,f) + P(\overline{s})*R(\overline{s},f) $$

and the expected reward of not firing would be 

$$ E(\overline{f}) = P(s)*R(s,\overline{f}) + P(\overline{s})*R(\overline{s},\overline{f}) $$

Now, plugging in our values of reward and probability, we get - 

$$ E(f) = 0.04*(10000 + 0.8 * 5L) + 0.96*(0.8 * 5L) = 4.004L $$

and

$$ E(\overline{f}) = 0.04*(-10L) + 0.96*(5L) = 4.4L $$

The expected reward of not firing is **higher by a considerable amount, ~40K**. Which action would Mr. Maytan take? The one that **maximizes his expected reward**! And that would definitely be, **not firing** the employee. 

## Further Inference

<p align="center">
<img style="float: left; width: 50%;" src="https://sansiddhjain.github.io/graph4.svg">
<img style="float: left; width: 50%;;" src="https://sansiddhjain.github.io/graph5.svg">
</p>



<p align="center">
<i>Left : Positive reward for when the employee was fired and she spoke up is high, Right : Reward for when the employee was not fired and she spoke up is extremely negative</i>
</p>


The values I assumed were fairly conservative, and yet not firing the employee made more monetary sense by a fair margin. [This](https://www.livemint.com/Politics/AV3sIKoEBAGZozALMX8THK/99-cases-of-sexual-assaults-go-unreported-govt-data-shows.html) article from Mint says that less than 1% of the cases of sexual assault in India are reported. Taking that to be the probability of speaking up instead of 4%, we get \\(E(f, p(s) = 0.01) = 4.001\\), and \\(E(\overline{f},  p(s) = 0.01) = 4.85\\), which makes the decision making process all the more clear. Even if we assume that the PR shitstorm the company has to face if it chooses to not fire their employee, and the female employee does speak up, is existentially debilitating, something like 50L (usually occuring when the perpetrator is a high profile person and/or repeated offender), \\(E(\overline{f})\\) is still \\(4.45\\). If we assume that the reward the company gets for firing the perp before the female employee speaks up is really high due to the good PR they get, say 5L, even in that case, the difference between the expected rewards of not firing and firing is around **80,000**. From the standpoint of a business, which solely cares about maximising profits, and nothing else, it does not make sense to fire the perpetrator employee.

# What does this all mean?

What does all of this mean? What is the end result of going through this long, arduous, (and painstaking for some) process of modelling this situation mathematically? Well the key insight here is that, from the standpoint of maximising revenue, it does not make sense for the company to fire the perpetrator employee. And this applies to a wide range of "possible outcomes" - whether the PR shitstorm the company has to face is existentially devastating, or if it is mildly debilitating; whether the good PR the company gets in case they do the "morally right thing" is truly transformative, or just a pat on the back; and this doctrine even works in those industries where women speak up about transgressions a bit more in comparison to other places. And that makes sense if you think about it - it is a fact that not many companies consider it a moral responsibility to create an environment which is inclusive towards everyone in terms of safety, especially when that moral responsibility is at odds with revenue maximisation. Many company heads would agree that the actions they take are morally questionable, but they would cite how helpless they are because it is a ruthless world; they are answerable for their actions to investors, and therefore it is imperative for them to align all their actions with the goal of maximising profits. 
 
But wait, isn't this sort of a model too simplistic? Life is not as simple as a 2\*2 decision matrix; there are a plethora of actions you can take in a situation, resulting in a myriad of possibilities. True, this model is incorrect, if we are gauging the correctness of a model based on how precisely you are able to represent a situation. However, it is impossible to mathematically represent the complexities of human interactions in a completely accurate manner, and thus the goal of 100% precision is unattainable. Therefore the power of a mathematical model lies not in its capability of representation, but rather in its ability to help us make sense out of complex phenomena, and by enabling us to make smarter decisions in light of this understanding. And I believe this model is effective in helping us understand what the problem is, and what can we do about this.

But why is the reward for not firing the employee significantly greater? What is the single largest contributing factor for that, and what we can we do about it? The single largest contributing factor - women don't speak up. There is a significant negative reward associated with not firing the employee, when the female employee does subsequently speak up. However, because the probability of a woman speaking up is very low, there's little possibility of ending up in that situation, and people are willing to take a gamble and not fire that employee. Women are discouraged from speaking up for a variety of reasons, and with an even greater variety of excuses, and that subjugation enables the creation of a "safe haven" of sorts for the perpetrators. We have only considered the scenario where the perpetrator has economic importance in a large organisation; we have not even begun to talk about the case where the perpetrator is a direct superior of the victim, or when the perpetrator is a very senior person in the community. Threats like "I will ruin your career" are used to crush voices there. The perpetrators in almost all cases have leverage, and they are fully aware of that; they make it a point to abuse their power to crush any voices of retaliation, and create a culture of silent suffering. 

\#MeToo swept the world a year before, and it swept India the past week, and that is absolutely fantastic. However, the last thing I would want is for #MeToo to become a periodic event where people speak up about their horrifying stories, but things return to status quo a while after that. Fundamental cultural change where people start opening up more about incidents against them instinctively is something I would love to strive for. In our original decision tree model, if we assume the probability of women speaking up to be a variable, and calculate the situation when the rewards for firing and not firing the perpetrator to be equal, that probability turns out to be **6.62%** (**1.8%** in the case where the perpetrator may be high profile). So if we create a culture where even **7%** of the women end up speaking up about sexual transgressions, the company would rather fire the employee than keep him, irrespective of whether the female employee speaks up about the incident or not. Think about it - that's a fundamental cultural change. Just because the situation is such that simply reporting the perpetrator to the boss would put his career in jeopardy, so many people would think twice before committing a heinous act. 

So if you know someone who has been sexually assaulted, encourage them to speak up, and call out the predators, even. It may be daunting at first, but even if one person shows the courage of opening up, 10 others would follow. If we sustain that effort continously for a while, slowly and steadily, the culture would change, and we would have made life a tad bit better for everyone around.
