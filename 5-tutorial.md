
# Conditionals – Making Decisions

## {Introduction @unplugged}

In this lesson, you’ll learn how to make your @boardname@ **think and decide** using **if / else conditionals**.

A conditional is a question with two possible answers:

* YES (true)
* NO (false)

By the end, your @boardname@ will change its behaviour depending on how fast it is moving or which button is pressed.

---

## {Step 1}

We will check how fast the @boardname@ is moving using the **accelerometer**.

From ``||input:Input||`` drag out:
``||input:acceleration (strength)||``

This block gives a **number** that shows movement strength.

Now from ``||logic:Logic||`` get:
``||logic:if / else||``

Put the **acceleration (strength)** block into the **condition** of the if:

```blocks
input.acceleration(Dimension.Strength) > 800
```

This is asking:

> “Is the movement stronger than 800?”

---

## {Step 2}

Now we decide what to do **if it is true or false**.

Inside the **if** part:
``||basic:show icon SAD||`` 😞

Inside the **else** part:
``||basic:show icon HAPPY||`` 🙂

Put the whole **if / else** block inside:
``||input:on shake||``

```blocks
input.onGesture(Gesture.Shake, function () {
    if (input.acceleration(Dimension.Strength) > 800) {
        //@highlight
        basic.showIcon(IconNames.Sad)
    } else {
        //@highlight
        basic.showIcon(IconNames.Happy)
    }
})
```

Now test:
* Gentle shake → 🙂
* Strong shake → 😞

---

## {Step 3}

Let’s add another conditional using **Button A**.

From ``||input:Input||`` get:
``||input:on button A pressed||``

Inside it, add another **if / else**. Use the same condition:

```blocks
input.onButtonPressed(Button.A, function () {
    if (input.acceleration(Dimension.Strength) > 800) {
        //@highlight
        basic.showString("FAST")
    } else {
        //@highlight
        basic.showString("SLOW")
    }
})
```

Press **Button A** to check your speed.

---

## {Step 4}

Experiment by changing the number **800** to:

* 500 (more sensitive)
* 1200 (less sensitive)

Which one works best?

---

## {Step 5 – Challenges}

Try one or more of these:

* Button B shows **TOO FAST** or **SAFE**
* If speed is high → play a warning sound 🔊
* Show a warning symbol (⚠️) instead of text
* Create a "speed detector" game with levels

---

## {Step 6}

If you have a @boardname@, connect it and click ``|Download|`` to try it in the real world.

Shake it. Test it. Improve it.

You just taught a computer how to **make decisions** 🧠✨

```validation.global
# BlocksExistValidator
```

```template
input.onGesture(Gesture.Shake, function () {
})
```

