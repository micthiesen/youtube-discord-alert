import { Component } from "solid-js";
import { useStore } from "../state";

const FlashMessage: Component = () => {
  const state = useStore();
  return state.flashMessage ? (
    <div>
      <span>{state.flashMessage}</span>
    </div>
  ) : null;
};

export default FlashMessage;
