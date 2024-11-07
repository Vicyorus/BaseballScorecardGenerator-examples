import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-06-13
# https://www.baseball-reference.com/boxes/BAL/BAL201306130.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/06/13/347734/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-13 19:07-23:42",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "20,098",
        "temp": "75F, Cloudy",
        "wind": "3mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                22: "Felix Doubront",
                # Bench
                3: "David Ross",
                37: "Mike Carp",
                10: "Jose Iglesias",
                5: "Jonny Gomes",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 30, 32, 31],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [3, "C"],
                [37, "1B"],
                [10, "2B"],
                [5, "LF"],
            ],
            "bullpen": [63, 40, 41, 56, 30, 32, 19, 31, 36, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 37,
            "roster": {
                # Lineup
                9: "Nate McLouth",
                13: "Manny Machado",
                21: "Nick Markakis",
                10: "Adam Jones",
                19: "Chris Davis",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                35: "Danny Valencia",
                3: "Ryan Flaherty",
                # Starting pitcher
                37: "Kevin Gausman",
                # Bench
                28: "Steve Pearce",
                31: "Taylor Teagarden",
                36: "Chris Dickerson",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                47: "Pedro Strop",
                38: "Freddy Garcia",
                29: "Tommy Hunter",
                56: "Darren O'Day",
                39: "Jason Hammel",
                17: "Brian Matusz",
                43: "Jim Johnson",
            },
            "lefties": [40, 66, 17],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [21, "9"],
                [10, "8"],
                [19, "3"],
                [32, "2"],
                [2, "6"],
                [35, "0"],
                [3, "4"],
            ],
            "bench": [
                [28, "1B"],
                [31, "C"],
                [36, "LF"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 47, 38, 29, 56, 39, 17, 43],
        },
        "umpires": {
            "HP": "Jim Joyce",
            "1B": "Cory Blaser",
            "2B": "Jeff Nelson",
            "3B": "Mike Estabrook",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BAL #37 Kevin Gausman
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.thrown_out(1, "15 DP5-3", 3, 37)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("b b f 1 f b")
t1.out("DP5-3")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("(F)P2")

# 2. BAL #13 Manny Machado (X - X - X)
b1.new_ab()
b1.out("G6-3")

# 3. BAL #21 Nick Markakis (X - X - X)
b1.new_ab()
b1.pitch_list("c c b c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #37 Kevin Gausman
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b s")
t2.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b s b b t")
t2.hit(2)

# 6. BOS #29 Daniel Nava (X - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b c t s")
t2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c f c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("G6-3")

# 5. BAL #19 Chris Davis (X - X - X)
b2.new_ab()
b2.reach("HBP")

# 6. BAL #32 Matt Wieters (X - X - 19)
b2.new_ab()
b2.pitch_list("b")
b2.out("(F)P4")

# 7. BAL #2  J.J. Hardy (X - X - 19)
b2.new_ab()
b2.pitch_list("1 c b b")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #37 Kevin Gausman
t3 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t3.new_ab()
t3.pitch_list("b c f f b b")
t3.out("G5-3")

# 9. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("b s b")
t3.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("f c b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# Defensive change (BOS): #37 Mike Carp replaces #12 Mike Napoli (1B), playing 1B, batting 5th
b3.defensive_substitution(5, 37, "3")

# 8. BAL #35 Danny Valencia (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(4)

# 9. BAL #3  Ryan Flaherty (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(2)
b3.advance(3, "9 SAC1-3")
b3.advance(4, "13 1B")

# 1. BAL #9  Nate McLouth (X - 3 - X)
b3.new_ab(is_risp=True)
b3.out("SAC1-3")

# 2. BAL #13 Manny Machado (3 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f b f")
b3.hit(1, rbis=1)
b3.advance(2, "21 1B")
b3.advance(3, "10 FC3-6")
b3.advance(4, "19 1B")

# 3. BAL #21 Nick Markakis (X - X - 13)
b3.new_ab()
b3.pitch_list("b 1 c b f")
b3.hit(1)
b3.thrown_out(2, "10 FC3-6", 2, 22)

# 4. BAL #10 Adam Jones (X - 13 - 21)
b3.new_ab(is_risp=True)
b3.reach("FC3-6")
b3.advance(2, "19 1B")

# 5. BAL #19 Chris Davis (13 - X - 10)
b3.new_ab(is_risp=True)
b3.pitch_list("b c")
b3.hit(1, rbis=1)

# 6. BAL #32 Matt Wieters (X - 10 - 19)
b3.new_ab(is_risp=True)
b3.pitch_list("b b f f d c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #37 Kevin Gausman
t4 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t4.new_ab()
t4.pitch_list("c f f b b f s")
t4.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(4)

# 5. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("c s b f b")
t4.hit(4)

# 6. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.out("L4")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 7. BAL #2  J.J. Hardy (X - X - X)
b4.new_ab()
b4.pitch_list("b b f c f b")
b4.out("P4")

# 8. BAL #35 Danny Valencia (X - X - X)
b4.new_ab()
b4.pitch_list("c b b c f b f")
b4.hit(2)

# 9. BAL #3  Ryan Flaherty (X - 35 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c f f s")
b4.out("K")

# 1. BAL #9  Nate McLouth (X - 35 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c s f b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #37 Kevin Gausman
t5 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c c b b")
t5.hit(2)

# 9. BOS #7  Stephen Drew (X - 16 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b f f")
t5.out("L1")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b")
t5.out("G3")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
b5.new_ab()
b5.pitch_list("c c b f")
b5.out("F9")

# 3. BAL #21 Nick Markakis (X - X - X)
b5.new_ab()
b5.pitch_list("b b c s b")
b5.error(5)
b5.reach("E5")
b5.advance(2, "10 HBP")
b5.advance("U", "32 1B")

# 4. BAL #10 Adam Jones (X - X - 21)
b5.new_ab()
b5.pitch_list("b s f b")
b5.reach("HBP")
b5.advance(3, "32 1B")

# 5. BAL #19 Chris Davis (X - 21 - 10)
b5.new_ab(is_risp=True)
b5.pitch_list("s s b f f s")
b5.out("K")

# 6. BAL #32 Matt Wieters (X - 21 - 10)
b5.new_ab(is_risp=True)
b5.pitch_list("d b b c s")
b5.hit(1, rbis=1)
b5.advance(2, "2 BB")

# 7. BAL #2  J.J. Hardy (10 - X - 32)
b5.new_ab(is_risp=True)
b5.pitch_list("c f b b f b b")
b5.reach("BB")

# Pitching change (BOS): #56 Franklin Morales replaces #22 Felix Doubront
b5.pitching_substitution(56)

# 8. BAL #35 Danny Valencia (10 - 32 - 2)
b5.new_ab(is_risp=True)
b5.pitch_list("d c s b")
b5.out("P6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #37 Kevin Gausman
t6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c c")
t6.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c b b")
t6.hit(1)

# Pitching change (BAL): #17 Brian Matusz replaces #37 Kevin Gausman
t6.pitching_substitution(17)

# 4. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.out("P6")

# 5. BOS #37 Mike Carp (X - X - 15)
t6.new_ab()
t6.pitch_list("b d s b t c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #56 Franklin Morales
b6 = game.new_inning()

# 9. BAL #3  Ryan Flaherty (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G2-3")

# 1. BAL #9  Nate McLouth (X - X - X)
b6.new_ab()
b6.reach("HBP")
b6.advance(2, "13 1B")

# 2. BAL #13 Manny Machado (X - X - 9)
b6.new_ab()
b6.pitch_list("c 1 b b s f")
b6.hit(1)

# 3. BAL #21 Nick Markakis (X - 9 - 13)
b6.new_ab(is_risp=True)
b6.pitch_list("b b")
b6.out("L8")

# 4. BAL #10 Adam Jones (X - 9 - 13)
b6.new_ab(is_risp=True)
b6.pitch_list("f d b c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #17 Brian Matusz
t7 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t7.new_ab()
t7.hit(1)
t7.advance(2, "39 1B")
t7.advance(3, "16 1B")
t7.advance(4, "7 SF8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)
t7.advance(2, "16 1B")
t7.advance(3, "7 SF8")
t7.advance(4, "2 FC4-6")

# 8. BOS #16 Will Middlebrooks (X - 29 - 39)
t7.new_ab(is_risp=True)
t7.pitch_list("s c d d f f")
t7.hit(1)
t7.thrown_out(2, "2 FC4-6", 2, 17)

# 9. BOS #7  Stephen Drew (29 - 39 - 16)
t7.new_ab(is_risp=True)
t7.pitch_list("s c f")
t7.out("SF8", rbis=1)

# 1. BOS #2  Jacoby Ellsbury (39 - X - 16)
t7.new_ab(is_risp=True)
t7.pitch_list("c f b f")
t7.reach("FC4-6", rbis=1)
t7.thrown_out(2, "18 CS", 3, 29)

# Pitching change (BAL): #29 Tommy Hunter replaces #17 Brian Matusz
t7.pitching_substitution(29)

# 2. BOS #18 Shane Victorino (X - X - 2)
t7.new_ab()
t7.pitch_list("1 c 1 1 c")
t7.no_ab("CS")


# Bot 7th
# Pitching: BOS #30 Andrew Miller
b7 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #56 Franklin Morales
b7.pitching_substitution(30)

# 5. BAL #19 Chris Davis (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")

# 6. BAL #32 Matt Wieters (X - X - X)
b7.new_ab()
b7.pitch_list("s s f c")
b7.out("!K")

# 7. BAL #2  J.J. Hardy (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b b")
b7.reach("BB")

# 8. BAL #35 Danny Valencia (X - X - 2)
b7.new_ab()
b7.pitch_list("f b s c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #29 Tommy Hunter
t8 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("G3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.out("F9")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("f s")
t8.out("P5")


# Bot 8th
# Pitching: BOS #30 Andrew Miller
b8 = game.new_inning()

# 9. BAL #3  Ryan Flaherty (X - X - X)
b8.new_ab()
b8.out("G4-3")

# 1. BAL #9  Nate McLouth (X - X - X)
b8.new_ab()
b8.pitch_list("b f c b f b b")
b8.reach("BB")

# 2. BAL #13 Manny Machado (X - X - 9)
b8.new_ab()
b8.pitch_list("1 1 b")
b8.out("L8")

# 3. BAL #21 Nick Markakis (X - X - 9)
b8.new_ab()
b8.pitch_list("t 1 f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #29 Tommy Hunter
t9 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
t9.new_ab()
t9.pitch_list("f f c")
t9.out("!K")

# 6. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("G5-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("s s f b f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #36 Junichi Tazawa
b9 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #30 Andrew Miller
b9.pitching_substitution(36)

# 4. BAL #10 Adam Jones (X - X - X)
b9.new_ab()
b9.out("(F)P6")

# 5. BAL #19 Chris Davis (X - X - X)
b9.new_ab()
b9.pitch_list("s b f b b f")
b9.out("P6")

# 6. BAL #32 Matt Wieters (X - X - X)
b9.new_ab()
b9.hit(1)
b9.error(9)
b9.advance(2, "E9")

# 7. BAL #2  J.J. Hardy (X - 32 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("d")
b9.out("(F)P2")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BAL #56 Darren O'Day
t10 = game.new_inning()

# Pitching change (BAL): #56 Darren O'Day replaces #29 Tommy Hunter
t10.pitching_substitution(56)

# 8. BOS #16 Will Middlebrooks (X - X - X)
t10.new_ab()
t10.pitch_list("c f c")
t10.out("!K")

# 9. BOS #7  Stephen Drew (X - X - X)
t10.new_ab()
t10.pitch_list("c c")
t10.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t10.new_ab()
t10.pitch_list("b f b f b f f f n")
t10.error(2)
t10.reach("CI")
t10.advance(2, "18 SB")

# 2. BOS #18 Shane Victorino (X - X - 2)
t10.new_ab(is_risp=True)
t10.pitch_list("b c f f f b f b s")
t10.out("K")


# Bot 10th
# Pitching: BOS #36 Junichi Tazawa
b10 = game.new_inning()

# 8. BAL #35 Danny Valencia (X - X - X)
b10.new_ab()
b10.pitch_list("s")
b10.out("F9")

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b10.pitching_substitution(32)

# 9. BAL #3  Ryan Flaherty (X - X - X)
b10.new_ab()
b10.pitch_list("b f b b f f c")
b10.out("!K")

# 1. BAL #9  Nate McLouth (X - X - X)
b10.new_ab()
b10.pitch_list("b b f b b")
b10.reach("BB")
b10.thrown_out(2, "13 FC6-4", 3, 32)

# 2. BAL #13 Manny Machado (X - X - 9)
b10.new_ab()
b10.reach("FC6-4")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BAL #56 Darren O'Day
t11 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t11.new_ab()
t11.pitch_list("b f")
t11.out("G6-3")

# Pitching change (BAL): #40 Troy Patton replaces #56 Darren O'Day
t11.pitching_substitution(40)

# 4. BOS #34 David Ortiz (X - X - X)
t11.new_ab()
t11.out("F8")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 5th
t11.offensive_substitution(5, 5, "PH")

# 5. BOS #5  Jonny Gomes (X - X - X)
t11.new_ab()
t11.pitch_list("c b b")
t11.out("G5-3")


# Bot 11th
# Pitching: BOS #63 Alex Wilson
b11 = game.new_inning()

# Pitching change (BOS): #63 Alex Wilson replaces #32 Craig Breslow
b11.pitching_substitution(63)

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b11.defensive_switch(5, "7")

# Defensive switch (BOS): #29 Daniel Nava moves to 1B
b11.defensive_switch(29, "3")

# 3. BAL #21 Nick Markakis (X - X - X)
b11.new_ab()
b11.out("F7")

# 4. BAL #10 Adam Jones (X - X - X)
b11.new_ab()
b11.pitch_list("s")
b11.out("P2")

# 5. BAL #19 Chris Davis (X - X - X)
b11.new_ab()
b11.pitch_list("c s b b b s")
b11.out("K")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: BAL #43 Jim Johnson
t12 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #40 Troy Patton
t12.pitching_substitution(43)

# 6. BOS #29 Daniel Nava (X - X - X)
t12.new_ab()
t12.pitch_list("c b f b b")
t12.out("G4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t12.new_ab()
t12.out("G1-3")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t12.new_ab()
t12.pitch_list("c c")
t12.out("L1-3")


# Bot 12th
# Pitching: BOS #63 Alex Wilson
b12 = game.new_inning()

# 6. BAL #32 Matt Wieters (X - X - X)
b12.new_ab()
b12.pitch_list("b f f")
b12.out("F8")

# 7. BAL #2  J.J. Hardy (X - X - X)
b12.new_ab()
b12.out("G4-3")

# Offensive change (BAL): Pinch-hitter #36 Chris Dickerson replaces #35 Danny Valencia, batting 8th
b12.offensive_substitution(8, 36, "PH")

# 8. BAL #36 Chris Dickerson (X - X - X)
b12.new_ab()
b12.pitch_list("c b")
b12.hit(2)

# 9. BAL #3  Ryan Flaherty (X - 36 - X)
b12.new_ab(is_risp=True)
b12.pitch_list("c")
b12.out("F9")


##########################################################
# 13th Inning
##########################################################
# Top 13th
# Pitching: BAL #66 T.J. McFarland
t13 = game.new_inning()

# Pitching change (BAL): #66 T.J. McFarland replaces #43 Jim Johnson
t13.pitching_substitution(66)

# Defensive switch (BAL): #36 Chris Dickerson moves to DH
t13.defensive_switch(36, "0")

# 9. BOS #7  Stephen Drew (X - X - X)
t13.new_ab()
t13.pitch_list("c f b b s")
t13.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t13.new_ab()
t13.pitch_list("b b f")
t13.out("G3")

# 2. BOS #18 Shane Victorino (X - X - X)
t13.new_ab()
t13.pitch_list("f f b f b f")
t13.out("F8")


# Bot 13th
# Pitching: BOS #63 Alex Wilson
b13 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
b13.new_ab()
b13.pitch_list("c b b c t")
b13.out("KT")

# 2. BAL #13 Manny Machado (X - X - X)
b13.new_ab()
b13.pitch_list("s c")
b13.out("G5-3")

# 3. BAL #21 Nick Markakis (X - X - X)
b13.new_ab()
b13.pitch_list("b c b c b b")
b13.reach("BB")
b13.advance(2, "10 1B")
b13.advance(4, "19 1B")

# 4. BAL #10 Adam Jones (X - X - 21)
b13.new_ab()
b13.pitch_list("f b c")
b13.hit(1)
b13.advance(2, "19 1B")

# 5. BAL #19 Chris Davis (X - 21 - 10)
b13.new_ab(is_risp=True)
b13.pitch_list("b s")
b13.hit(1, rbis=1)

# Winning team: BAL
# WP: BAL #66 T.J. McFarland
game.winning_pitcher(66)

# Loser team: BOS
# LP: BOS #63 Alex Wilson
game.losing_pitcher(63, is_away_team=True)

# print(game)
game.generate_scorecard()
