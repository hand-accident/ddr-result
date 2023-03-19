<script>
    let className, dst;
    export { className as class, dst as for };
</script>

<label for={dst} class="c {className}">
    <slot />
</label>

<style lang="postcss" module>
    .c {
        @apply inline-flex flex-shrink-0 cursor-pointer select-none 
        flex-wrap items-center justify-center border-transparent text-center 
        transition duration-200 ease-in-out rounded-btn;
        @apply h-12 px-4 text-sm min-h-12;
        line-height: 1em;
        @apply font-semibold uppercase no-underline;
        border-width: var(--border-btn, 1px);
        animation: button-pop var(--animation-btn, 0.25s) ease-out;
        text-transform: var(--btn-text-case, uppercase);
        @apply border-info bg-info text-info-content;
    }
    .c:active:hover,
    .c:active:focus {
        animation: none;
        transform: scale(var(--btn-focus-scale, 0.95));
    }
    .c:hover,
    .c.btn-active {
        @apply border-info bg-info;
    }
    .c:focus-visible {
        outline: 2px solid hsl(var(--in));
    }
</style>
