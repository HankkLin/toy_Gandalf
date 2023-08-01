#!/usr/bin/env python
# coding: utf-8
# %%
import toy_example as toy
import gradio as gr


# %%
def checkAnswer(answer=""):
    if answer == toy.returnPassword():
        return True
    return False


# %%
def resetbtnclick(difficulty):
    toy.determineDifficulty(difficulty)
    return toy.choosePassword()


# %%
with gr.Blocks() as demo:
    
    
    title = "Gandolf - toy version"
    gr.Markdown("""
    # Toy Gandolf
    Use the left tab to ask question and right tab to chat""")
    
####################################################Turbo######################
    with gr.Tab("Ask Question (Turbo)"):
        question = gr.Textbox(label="Question!",placeholder = "Ask some question!", interactive = True)
        difficulty = gr.Radio(["Easy", "Medium", "Hard", "Hell"], label = "Difficulty", value = "Easy", interactive = True)
        response = gr.Textbox(label="Response", interactive = False)
        q_btn = gr.Button("Ask!")
        
    #Event listeners
    q_btn.click(fn=toy.returnAnswer, inputs=[question,difficulty], outputs=response)
    question.submit(fn=toy.returnAnswer, inputs=[question,difficulty], outputs=response)
        
#######################################Davinci#####################################
    with gr.Tab("Ask Question (Davinci)"):
            questionD = gr.Textbox(label="Question!",placeholder = "Ask some question!", interactive = True)
            difficultyD = gr.Radio(["Easy", "Medium", "Hard", "Hell"], label = "Difficulty", value = "Easy", interactive = True)
            responseD = gr.Textbox(label="Response", interactive = False)
            q_btnD = gr.Button("Ask!")
        
    #Event listeners
    q_btnD.click(fn=toy.GandolfDavinci, inputs=[difficultyD,questionD], outputs=responseD)
    questionD.submit(fn=toy.GandolfDavinci, inputs=[difficultyD,questionD], outputs=responseD)
        
#############################This part is chat ##############################
        
    with gr.Tab("Chat (Turbo)"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label = "What do you want to ask?")
        
        with gr.Row():
            chatDifficulty = gr.Radio(["Easy", "Medium", "Hard"], label = "Difficulty", value = "Hard", interactive = True)
            clear = gr.ClearButton([msg, chatbot], value = "Confirm Diffiulty and clear")
        
        def respond(message, chat_history):
            chat_history.append((message, toy.chat(message)))
            return "", chat_history #clear the textbox, and return the appended history

        #event listener
        msg.submit(fn = respond, inputs = [msg, chatbot], outputs = [msg, chatbot]) 
        clear.click(fn=toy.determineDifficulty, inputs = chatDifficulty)
    
############################# End of chat, password check #####################################
    with gr.Accordion("Password", open = False):
            answer = gr.Textbox(label="Enter the Password!", placeholder = "Password")
            result = gr.Textbox(label="Result", info = "True if the password is correct, False if not. Capitalize the first letter!")
            with gr.Row():
                a_btn = gr.Button("Enter!")
                reset_btn = gr.ClearButton([chatbot, msg], value ="Reset password")
        
            #Show password, just for testing
            with gr.Accordion("",open = False):
                a = gr.Textbox(label = "Password",value = toy.choosePassword())
       
    #event listener
    a_btn.click(fn=checkAnswer, inputs=answer, outputs=result)
    answer.submit(fn=checkAnswer, inputs=answer, outputs=result)
    reset_btn.click(fn=resetbtnclick, inputs=[chatDifficulty], outputs=a)

def launch():
    demo.launch(enable_queue=False, server_name="0.0.0.0") #server_port=6006



# %%
if __name__ == "__main__":
    launch()

# %%
