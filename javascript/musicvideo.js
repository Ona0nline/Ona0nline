// Im your man Mitski

let im_your_man_element = document.getElementById("iym");
    let im_your_man_button = document.getElementById("iym_button");

    function action_imym() {
      if (im_your_man_element.paused) {
        im_your_man_element.play();
        im_your_man_button.innerHTML = "Pause 'I'm your man'";
      } else {
        im_your_man_element.pause();
        im_your_man_button.innerHTML = "Play 'I'm your man'";
      }
    }

    // Garage rooftop
    let grg_roof_element = document.getElementById("grg");
    let garage_roof_button = document.getElementById("garage_roof");

    function action_grg() {
      if (grg_roof_element.paused) {
        grg_roof_element.play();
        garage_roof_button.innerHTML = "Pause 'Garage rooftop'";
      } else {
        grg_roof_element.pause();
        garage_roof_button.innerHTML = "Play 'Garage rooftop'";
      }
    }

    // You aint no celebrity

     let yanc_element = document.getElementById("yanc");
    let yanc_button = document.getElementById("yancc");

    function action_yanc() {
      if (yanc_element.paused) {
        yanc_element.play();
        yanc_button.innerHTML = "Pause 'You ain't no celebrity'";
      } else {
        yanc_element.pause();
        yanc_button.innerHTML = "Play 'You ain't no celebrity'";
      }
    }

    // Stronger
    let stronger_element = document.getElementById("stronger_video");
    let stronger_button = document.getElementById("str_button");

    function action_stronger() {
      if (stronger_element.paused) {
        stronger_element.play();
        stronger_button.innerHTML = "Pause 'Stronger'";
      } else {
        stronger_element.pause();
        stronger_button.innerHTML = "Play 'Stronger'";
      }
    }

    // Hold on

    let holdon_element = document.getElementById("holdon_video");
    let holdon_button = document.getElementById("holdon_button");

    function action_holdon() {
      if (holdon_element.paused) {
        holdon_element.play();
        holdon_button.innerHTML = "Pause 'Hold on'";
      } else {
        holdon_element.pause();
        holdon_button.innerHTML = "Play 'Hold on'";
      }
    }

     let lomelda_element = document.getElementById("lomelda_video");
    let lomelda_button = document.getElementById("lomelda_button");

    function action_lomelda() {
      if (lomelda_element.paused) {
        lomelda_element.play();
        lomelda_button.innerHTML = "Pause 'm for me'";
      } else {
        lomelda_element.pause();
        lomelda_button.innerHTML = "Play 'm for me'";
      }
    }

    
     let winehouse_element = document.getElementById("winehouse_video");
    let winehouse_button = document.getElementById("winehouse_button");

    function action_winehouse() {
      if (winehouse_element.paused) {
        winehouse_element.play();
        winehouse_button.innerHTML = "Pause 'Back to Black'";
      } else {
        winehouse_element.pause();
        winehouse_button.innerHTML = "Play 'Back to Black'";
      }
    }