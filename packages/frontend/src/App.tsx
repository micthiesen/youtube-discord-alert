import type { Component } from "solid-js";

import ChannelForm from "./components/ChannelForm";
import ChannelList from "./components/ChannelList";
import FlashMessage from "./components/FlashMessage";

const App: Component = () => (
  <div class="pb-3">
    <p class="font-fancy text-center text-white py-10 px-20 text-5xl">
      YouTube ➡️ Discord
    </p>
    <ChannelForm />
    <FlashMessage />
    <ChannelList />
  </div>
);

export default App;
