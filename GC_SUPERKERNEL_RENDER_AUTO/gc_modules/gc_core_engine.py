import time
from gc_modules import (
    gc_monetization_matrix,
    gc_cloneforge,
    gc_autoscaler,
    gc_sentient_core,
    gc_theme_mutator,
    gc_productlab_gpt,
    gc_ghost_commerce,
    gc_emopath_ai,
    gc_trendwatch_infinite,
    gc_account_creator,
    gc_notify_mindstream
)

def execute_mission_cycle(cycle):
    print(f"🌍 GC Core Engine - Cycle {cycle} lancé")
    gc_monetization_matrix.monetization_loop()
    if cycle % 2 == 0:
        gc_account_creator.mass_account_creation()
    if cycle % 3 == 0:
        gc_cloneforge.create_clone()
        gc_autoscaler.scale_channels()
    if cycle % 4 == 0:
        gc_productlab_gpt.generate_sellable_gpts()
    if cycle % 5 == 0:
        gc_ghost_commerce.launch_ghost_shop()
    if cycle % 6 == 0:
        gc_emopath_ai.interpret_emotion_and_convert()
    if cycle % 2 == 0:
        gc_theme_mutator.mutate_theme()
    gc_trendwatch_infinite.analyze_trends_infinitely()
    gc_sentient_core.sentient_thought()
    if cycle % 7 == 0:
        gc_notify_mindstream.send_report()

def start_gc_core_engine():
    print("🧠 GC Core Engine ACTIVÉ : Stratégie impériale en cours")
    cycle = 1
    while True:
        execute_mission_cycle(cycle)
        time.sleep(10)
        cycle += 1import threading

def launch_discord_bot():
    try:
        import gc_modules.gc_discord_bot as gc_bot
        exec(open("gc_modules/gc_discord_bot.py").read())
    except Exception as e:
        print(f"⚠️ Échec du lancement Discord Bot : {e}")

# Ajout du lancement du bot dans un thread parallèle
discord_thread = threading.Thread(target=launch_discord_bot)
discord_thread.start()